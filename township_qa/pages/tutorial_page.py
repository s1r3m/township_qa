from appium.webdriver.common.appiumby import AppiumBy

from township_qa.constants import IMAGE_PATH
from township_qa.helpers import Locator
from township_qa.pages.base import BasePage


class TutorialPage(BasePage):
    def _set_locators(self) -> None:
        self.ok_policy_button: Locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')
        # CV locators.
        self.ernie = IMAGE_PATH / 'ernie.png'
        self.empty_field = IMAGE_PATH / 'empty_field.png'
        self.empty_field_2 = IMAGE_PATH / 'empty_field_2.png'
        self.wheat = IMAGE_PATH / 'wheat.png'
        self.planted_wheat = IMAGE_PATH / 'planted_wheat.png'
        self.planted_wheat_2 = IMAGE_PATH / 'planted_wheat_2.png'

        self._indicator_element = self.ok_policy_button

    def start_tutorial(self) -> 'TutorialPage':
        button = self._page.find_element(*self.ok_policy_button)
        button.click()

        return self

    def tap_ernie(self) -> 'TutorialPage':
        ernie_face = self._vision.get_location(self.ernie)
        self._tapper.tap_image(ernie_face)

        return self

    def plant_wheat_on_empty_field(self) -> 'TutorialPage':
        empty_field = self._vision.get_location(self.empty_field, self.empty_field_2)
        self._tapper.tap_image(empty_field)
        wheat = self._vision.get_location(self.wheat)
        self._tapper.swipe(wheat, empty_field)

        return self

    def check_field_planted(self) -> None:
        planted_field = self._vision.get_location(self.planted_wheat, self.planted_wheat_2)
        assert planted_field
