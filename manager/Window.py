class Window:
    def __init__(self, str):
        windowProperties = list(filter(lambda str: str != "", str.split(" ")))

        self.hex = windowProperties[0]
        self.desktop = windowProperties[1]
        self.x = windowProperties[2]
        self.y = windowProperties[3]
        self.w = windowProperties[4]
        self.h = windowProperties[5]
        self.title = " ".join(windowProperties[6:])


def stringToWindows(windowsString):
    windows = windowsString.split("\n")
    return list(map(Window, windows))
