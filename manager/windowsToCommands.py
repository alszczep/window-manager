def windowToCommand(window, geometry):
    return "wmctrl -i -r \"{windowHex}\" -e 0,{x},{y},{w},{h}".format(windowHex = window.hex, x = geometry.x, y = geometry.y, w = geometry.w, h = geometry.h)

def windowsToCommands(windows, geometry):
    return list(map(lambda window: windowToCommand(window, geometry), windows))
