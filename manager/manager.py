from sys import argv
from generateCommand import *
from Geometry import *
from Settings import *

windowsString = argv[1]

settings = [
    Settings(
        "slack",
        Geometry(3840, 0, 1080, 689),
        maximize=False,
        ignoreMaximizeOff=False),
    Settings(
        "mozilla firefox",
        Geometry(3840, 718, 1080, 587),
        maximize=False,
        ignoreMaximizeOff=False),
    Settings(
        "konsole",
        Geometry(3840, 1363, 1080, 557),
        maximize=False,
        ignoreMaximizeOff=False),
    Settings(
        "google chrome",
        Geometry(1920, 420, 1920, 1036),
        maximize=True,
        ignoreMaximizeOff=False),
    Settings(
        "visual studio code",
        Geometry(0, 512, 1920, 1051),
        maximize=True,
        ignoreMaximizeOff=False),
]

print(generateCommand(settings, windowsString))
