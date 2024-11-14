# mypy: ignore-errors
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from township_qa.helpers import CvLocator


class DisplayClient:
    def __init__(self, page: WebDriver, duration: int):
        self.actions = ActionBuilder(page, duration=duration)

    def tap_image(self, image: CvLocator) -> None:
        self.actions.pointer_action.move_to_location(*image)
        self.actions.pointer_action.pointer_down()
        self.actions.pointer_action.pointer_up()
        self.actions.perform()

    def swipe(self, start: CvLocator, end: CvLocator) -> None:
        self.actions.pointer_action.move_to_location(*start)
        self.actions.pointer_action.pointer_down()
        self.actions.pointer_action.move_to_location(*end)
        self.actions.pointer_action.pointer_up()
        self.actions.perform()
