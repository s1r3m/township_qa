from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from settings import THRESHOLD, WAIT_TIMEOUT
from township_qa.clients.computer_vision import TownshipCV
from township_qa.clients.tapper import DisplayClient
from township_qa.helpers import Locator


class BasePage:
    _indicator_element: Locator  # An element that indicates that the page opened correctly

    def __init__(self, page: WebDriver):
        self._page = page
        self._vision = TownshipCV(THRESHOLD, WAIT_TIMEOUT)
        self._display = DisplayClient(page)
        self._set_locators()

        self._wait_loaded()

    def _wait_loaded(self) -> None:
        WebDriverWait(self._page, WAIT_TIMEOUT).until(EC.presence_of_element_located(self._indicator_element))

    def _set_locators(self) -> None:
        raise NotImplementedError('_set_locators should be implemented in child classes.')
