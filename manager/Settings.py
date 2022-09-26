import configparser
from Geometry import *


class Settings:
    def __init__(self, keyword, geometry, maximize, ignoreMaximizeOff):
        self.keyword = keyword
        self.geometry = geometry
        self.maximize = maximize
        self.ignoreMaximizeOff = ignoreMaximizeOff


def sectionToSettings(config, section):
    return Settings(
        section,
        Geometry(
            config[section]["x"],
            config[section]["y"],
            config[section]["w"],
            config[section]["h"]),
        maximize=config[section]["maximize"].lower() == "true",
        ignoreMaximizeOff=config[section]["ignoremaximizeoff"].lower() == "true")


def configToSettings(path):
    config = configparser.ConfigParser()
    config.read(path)
    return list(map(lambda section: sectionToSettings(config, section), config.sections()))
