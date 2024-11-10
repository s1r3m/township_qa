# APP_NAME = 'com.deepl.mobiletranslator'
from enum import Enum

APP_NAME = 'com.playrix.township'

APP_MAIN_ACTIVITY = '.GPlayActivity'
APP_START_ACTIVITY = '.Launcher'


class StrEnum(str, Enum):
    """Makes sure all elements are stings"""


class AppActivity(StrEnum):
    LAUNCHER = '.Launcher'
    PLAY = '.GPlayActivity'
