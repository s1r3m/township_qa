import os

DEBUG = os.environ.get("DEBUG", True)

DEVICE_NAME = os.environ.get("DEVICE_NAME", 'Nokia X20')
DEVICE_UDID = os.environ.get("DEVICE_UDID", 'AQKSLVH002M41600014')
PLATFORM_NAME = os.environ.get("PLATFORM_NAME", 'Android')
PLATFORM_VERSION = os.environ.get("PLATFORM_VERSION", '14')

WAIT_TIMEOUT = float(os.environ.get("WAIT_TIMEOUT", 40))
