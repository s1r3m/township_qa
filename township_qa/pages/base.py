from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._page = driver
