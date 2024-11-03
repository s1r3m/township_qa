from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, page: WebDriver):
        self._page = page
