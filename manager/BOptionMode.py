from enum import Enum


class BOptionMode(Enum):
    REMOVE = 1
    ADD = 2
    TOGGLE = 2


def modeToBOptionString(mode):
    if mode == BOptionMode.REMOVE:
        return "remove"
    if mode == BOptionMode.ADD:
        return "add"
    if mode == BOptionMode.TOGGLE:
        return "toggle"
