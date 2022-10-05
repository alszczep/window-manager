from manager.Window import *
from manager.findWindows import *
from manager.windowsToCommands import *
from common.mergeCommands import mergeCommands


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
