import sys
import generateCommand
import Geometry

windowsString = sys.argv[1]

settings = {
    "slack": Geometry.Geometry(3840, 0, 1080, 689),
    "mozilla firefox": Geometry.Geometry(3840, 718, 1080, 587),
    "konsole": Geometry.Geometry(3840, 1363, 1080, 557),
    "google chrome": Geometry.Geometry(1920, 420, 1920, 1036),
    "visual studio code": Geometry.Geometry(0, 512, 1920, 1051),
}

print(generateCommand.generateCommand(settings, windowsString))
