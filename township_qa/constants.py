from enum import Enum
from pathlib import Path

APP_NAME = 'com.playrix.township'

APP_MAIN_ACTIVITY = '.GPlayActivity'
APP_START_ACTIVITY = '.Launcher'

IMAGE_PATH = Path(__file__).parent / 'images'


class StrEnum(str, Enum):
    """Makes sure all elements are stings"""


class AppActivity(StrEnum):
    LAUNCHER = '.Launcher'
    PLAY = '.GPlayActivity'
