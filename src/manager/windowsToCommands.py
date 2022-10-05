from manager.BOptionMode import *


def windowToGeometryCommand(window, geometry):
    return "wmctrl -i -r \"{windowHex}\" -e 0,{x},{y},{w},{h}".format(
        windowHex=window.hex,
        x=geometry.x,
        y=geometry.y,
        w=geometry.w,
        h=geometry.h)


def windowsToGeometryCommands(windows, geometry):
    return list(map(lambda window: windowToGeometryCommand(window, geometry), windows))


def windowToMaximizeCommand(window, mode, dimension):
    return "wmctrl -i -r \"{windowHex}\" -b {mode},{dimension}".format(
        windowHex=window.hex,
        mode=modeToBOptionString(mode),
        dimension=dimension)


def windowsToMaximizeCommands(windows, mode):
    return list(map(lambda window: windowToMaximizeCommand(window, mode, "maximized_horz"), windows)
                ) + list(map(lambda window: windowToMaximizeCommand(window, mode, "maximized_vert"), windows))
