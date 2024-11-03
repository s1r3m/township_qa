from typing import Generator, TypeVar

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

from settings import DEBUG, DEVICE_NAME, DEVICE_UDID, PLATFORM_NAME, PLATFORM_VERSION
from township_qa.constants import APP_NAME, APP_START_ACTIVITY
from township_qa.pages.main_page import MainPage

T = TypeVar('T')
YieldFixture = Generator[T, None, None]


@pytest.fixture
def driver() -> YieldFixture[WebDriver]:
    options = AppiumOptions()
    options.set_capability('platformName', PLATFORM_NAME)
    options.set_capability('platformVersion', PLATFORM_VERSION)
    options.set_capability('deviceName', DEVICE_NAME)
    options.set_capability('udid', DEVICE_UDID)
    options.set_capability('appPackage', APP_NAME)
    options.set_capability('printPageSourceOnFindFailure', DEBUG)
    options.set_capability('appActivity', APP_START_ACTIVITY)
    options.set_capability('automationName', 'UiAutomator2')
    driver = webdriver.Remote('http://localhost:4723', options=options)

    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver) -> MainPage:
    page = MainPage(driver)
    page._wait_page_loaded()
    return page
