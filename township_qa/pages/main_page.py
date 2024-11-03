from selenium.webdriver.common.by import By

from township_qa.pages.base import BasePage


class MainPage(BasePage):
    START_BUTTON = (By.ID, 'start_button')

    def start_tutorial(self) -> 'MainPage':
        start_button = self._page.find_element(*self.START_BUTTON)
        start_button.click()
        return self

    def check_activity(self, expected_activity: str) -> None:
        assert self._page.current_activity == expected_activity
