# from sys import argv
from manager.generateCommand import generateCommand
from manager.Settings import configToSettings

# windowsString = argv[1]
# configPath = argv[2]


def manager(windowsString, configPath):
    settings = configToSettings(configPath)

    print(generateCommand(settings, windowsString))
