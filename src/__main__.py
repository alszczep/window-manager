from sys import argv
from manager.manager import manager
from helpers.getKillKscreenCommand import getKillKscreenCommand

mode = argv[1]

if mode == "manager":
    manager(windowsString=argv[2], configPath=argv[3])
elif mode == "killKscreen":
    getKillKscreenCommand(processString=argv[2])
else:
    print("echo Mode is incorrect")
