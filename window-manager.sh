#!/bin/bash

function usage {
        echo "Usage: $(basename $0) [-k] [-p PATH]"
        echo
        echo "Mandatory:"
        echo "   -p   path to the window-manager folder"
        echo
        echo "Options:"
        echo "   -k   kill kscreen process"
        exit 1
}

if [[ $# -eq 0 ]]
then
   usage
fi

while getopts ":hp:k" arg
do
    case "${arg}" in
        h) usage ;;
        p) windowManagerPath="${OPTARG}" ;;
        k) kscreenProcessString=`ps aux | grep kscreen_backend_launcher | grep -v "grep"` ;;

        ?)
            echo "Invalid option: -${OPTARG}."
            echo
            usage
            ;;
    esac
done

if [[ -z ${windowManagerPath} ]]
then
    echo "Argument -p is mandatory"
    echo
    usage
fi

if [[ -n ${kscreenProcessString} ]]
then
    killKscreenCommand=`python3 "${windowManagerPath}/helpers/getKillKscreenCommand.py" "${kscreenProcessString}"`
    eval "${killKscreenCommand}"
fi

windows=`wmctrl -p -G -l`
managerCommand=`python3 "${windowManagerPath}/manager/manager.py" "${windows}"`
eval "${managerCommand}"
