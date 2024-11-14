import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

from settings import APPIUM_HOST, AUTOMATION_NAME, DEBUG, DEVICE_NAME, DEVICE_UDID, PLATFORM_NAME, PLATFORM_VERSION
from township_qa.constants import APP_NAME, AppActivity
from township_qa.helpers import YieldFixture
from township_qa.pages.tutorial_page import TutorialPage


@pytest.fixture
def driver() -> YieldFixture[WebDriver]:
    options = AppiumOptions()
    options.set_capability('platformName', PLATFORM_NAME)
    options.set_capability('platformVersion', PLATFORM_VERSION)
    options.set_capability('deviceName', DEVICE_NAME)
    options.set_capability('udid', DEVICE_UDID)
    options.set_capability('appPackage', APP_NAME)
    options.set_capability('printPageSourceOnFindFailure', DEBUG)
    options.set_capability('appActivity', AppActivity.LAUNCHER)
    options.set_capability('automationName', AUTOMATION_NAME)
    driver = webdriver.Remote(APPIUM_HOST, options=options)

    yield driver

    driver.quit()


@pytest.fixture
def tutorial_page(driver: WebDriver) -> TutorialPage:
    tutorial_page = TutorialPage(driver)
    tutorial_page = tutorial_page.start_tutorial()

    return tutorial_page
