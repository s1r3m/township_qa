from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import WAIT_TIMEOUT
from township_qa.pages.base import BasePage


class MainPage(BasePage):
    OK_POLICY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')

    def __init__(self, page: WebDriver):
        super().__init__(page)

    def _wait_page_loaded(self) -> 'MainPage':
        accept_button = WebDriverWait(self._page, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.OK_POLICY_BUTTON)
        )
        accept_button.click()
        return self

    def start_tutorial(self) -> 'MainPage':
        pass

    def check_activity(self, expected_activity: str) -> None:
        assert self._page.current_activity == expected_activity
