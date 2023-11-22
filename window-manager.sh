#!/bin/bash

function usage {
        echo "Usage: $(basename $0) [-p PATH] [-c PATH]"
        echo
        echo "   -p   path to the window-manager folder"
        echo "   -c   path to the .ini config file"
        exit 1
}

if [[ $# -eq 0 ]]
then
   usage
fi

while getopts ":hp:c:" arg
do
    case "${arg}" in
        h) usage ;;
        p) windowManagerPath="${OPTARG}" ;;
        c) configPath="${OPTARG}" ;;

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

if [[ -z ${configPath} ]]
then
    echo "Argument -c is mandatory"
    echo
    usage
fi

windows=`wmctrl -Gl`
managerCommand=`python3 "${windowManagerPath}/src/__main__.py" "manager" "${windows}" "${configPath}"`
eval "${managerCommand}"
