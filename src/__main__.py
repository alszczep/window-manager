from sys import argv
from manager.manager import manager

mode = argv[1]

if mode == "manager":
    manager(windowsString=argv[2], configPath=argv[3])
else:
    print("echo Mode is incorrect")
