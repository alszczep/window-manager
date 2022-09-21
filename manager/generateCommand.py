import Window
import findWindows
import windowsToCommands

def mergeCommands(commands):
    return " && ".join(commands)

def generateCommand(settings, windowsString):
    allWindows = Window.stringToWindows(windowsString)

    allCommands = []

    for key, geometry in settings.items():
        foundWindows = findWindows.findWindowsByTitleString(key, allWindows)
        commands = windowsToCommands.windowsToCommands(foundWindows, geometry)
        allCommands += commands

    return mergeCommands(allCommands)
