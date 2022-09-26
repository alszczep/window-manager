class Window:
    def __init__(self, str):
        windowProperties = list(filter(lambda str: str != "", str.split(" ")))

        self.hex = windowProperties[0]
        self.desktop = windowProperties[1]
        self.dec = windowProperties[2]
        self.x = windowProperties[3]
        self.y = windowProperties[4]
        self.w = windowProperties[5]
        self.h = windowProperties[6]
        self.title = " ".join(windowProperties[7:])


def stringToWindows(windowsString):
    windows = windowsString.split("\n")
    return list(map(Window, windows))
