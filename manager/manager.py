from sys import argv
from generateCommand import generateCommand
from Settings import configToSettings

windowsString = argv[1]
configPath = argv[2]

settings = configToSettings(configPath)

print(generateCommand(settings, windowsString))
