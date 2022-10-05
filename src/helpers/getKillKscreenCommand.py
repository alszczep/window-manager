def getKillKscreenCommand(processString):
    processProperties = list(
        filter(lambda str: str != "", processString.split(" ")))
    pid = processProperties[1]

    print("kill {pid}".format(pid=pid))
