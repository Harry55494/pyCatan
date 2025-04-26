from src.version import *


VERSION_FULL = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
VERSION_DISPLAY = f"pyCatan {VERSION_FULL}"


def get_version():
    return VERSION_FULL


def get_version_display():
    return VERSION_DISPLAY
