from src.version import *
import warnings


def get_ascii_title():
    with warnings.catch_warnings(action="ignore"):
        return "\n                  ______      __ \n     ____  __  __/ ____/___ _/ / _____ _____ \n    / __ \/ / / / /   / __ `/ __/ __ `/ __ `/ \n   / /_/ / /_/ / /___/ /_/ / /_/ /_/ / / / / \n  / .___/\__, /\____/\__,_/\__/\__,_/_/ /_/ \n /_/    /____/    \n"


VERSION_FULL = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
VERSION_DISPLAY = f"pyCatan {VERSION_FULL}"


def get_version():
    return VERSION_FULL


def get_version_display():
    return VERSION_DISPLAY


def get_repo_info():
    return "https://github.com/Harry55494/pyCatan"
