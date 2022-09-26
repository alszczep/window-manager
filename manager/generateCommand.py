from Window import *
from findWindows import *
from windowsToCommands import *


def mergeCommands(commands):
    return " && ".join(commands)


def generateCommand(settings, windowsString):
    allWindows = stringToWindows(windowsString)

    allCommands = []

    for setting in settings:
        foundWindows = findWindowsByTitleString(setting.keyword, allWindows)

        maximizeOffCommands = []
        if not setting.ignoreMaximizeOff:
            maximizeOffCommands = windowsToMaximizeCommands(
                foundWindows, BOptionMode.REMOVE)

        geometryCommands = windowsToGeometryCommands(
            foundWindows, setting.geometry)

        maximizeOnCommands = []
        if setting.maximize:
            maximizeOnCommands = windowsToMaximizeCommands(
                foundWindows, BOptionMode.ADD)

        allCommands += maximizeOffCommands + geometryCommands + maximizeOnCommands

    return mergeCommands(allCommands)
