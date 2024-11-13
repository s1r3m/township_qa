from appium.webdriver.common.appiumby import AppiumBy

from township_qa.constants import AppActivity
from township_qa.helpers import Locator
from township_qa.pages.base import BasePage


class TutorialPage(BasePage):
    def _set_locators(self) -> None:
        self.ok_policy_button: Locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')

        self._indicator_element = self.ok_policy_button

    def check_activity(self, expected_activity: AppActivity) -> None:
        assert self._page.current_activity == expected_activity
