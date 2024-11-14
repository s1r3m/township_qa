import os

DEBUG = os.environ.get('DEBUG', True)

APPIUM_HOST = os.environ.get('APPIUM_HOST', 'http://localhost:4723')
AUTOMATION_NAME = os.environ.get('AUTOMATION_NAME', 'UiAutomator2')
DEVICE_NAME = os.environ.get('DEVICE_NAME', 'Nokia X20')
DEVICE_UDID = os.environ.get('DEVICE_UDID', 'AQKSLVH002M41600014')
PLATFORM_NAME = os.environ.get('PLATFORM_NAME', 'Android')
PLATFORM_VERSION = os.environ.get('PLATFORM_VERSION', '14')

DISPLAY_ACTION_DURATION = os.environ.get('DISPLAY_ACTION_DURATION', 750)
THRESHOLD = float(os.environ.get('THRESHOLD', 0.7))
WAIT_TIMEOUT = float(os.environ.get('WAIT_TIMEOUT', 20))
WAIT_INTERVAL = float(os.environ.get('WAIT_INTERVAL', 0.1))
