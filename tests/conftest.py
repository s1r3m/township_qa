import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

from settings import DEVICE_NAME, DEVICE_UDID, PLATFORM_NAME, PLATFORM_VERSION
from township_qa.constants import APP_NAME
from township_qa.pages.main_page import TownshipMainPage


@pytest.fixture
def driver():
    options = AppiumOptions()
    options.set_capability("platformName", PLATFORM_NAME)
    options.set_capability("platformVersion", PLATFORM_VERSION)
    options.set_capability("deviceName", DEVICE_NAME)
    options.set_capability("udid", DEVICE_UDID)
    options.set_capability("appPackage", APP_NAME)
    options.set_capability("appActivity", ".MainActivity")
    options.set_capability("automationName", "UiAutomator2")
    driver: WebDriver = webdriver.Remote('http://localhost:4723', options=options)

    yield driver

    driver.quit()


@pytest.fixture
def main_page(driver):
    page = TownshipMainPage(driver)
    return page
