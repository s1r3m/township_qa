import subprocess
import time
from pathlib import Path

import cv2
import numpy as np
from cv2.typing import MatLike

from township_qa.helpers import Coordinates


class TownshipCV:
    def __init__(self, threshold: float, timeout: float):
        self.threshold = threshold
        self.timeout = timeout
        self.interval = 0.1

    def get_location(self, *image_files: Path) -> Coordinates:
        images = []
        for image_file in image_files:
            if not image_file.is_file():
                raise FileNotFoundError(f'{image_file} is not found!')
            images.append(cv2.imread(str(image_file)))
        locations = self._wait_for_image(*images)
        return locations

    @staticmethod
    def _get_screenshot() -> MatLike:
        subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screen.png'], check=True)
        subprocess.run(['adb', 'pull', '/sdcard/screen.png'], check=True)
        image = cv2.imread('screen.png')
        return image

    def _wait_for_image(self, *images: MatLike) -> Coordinates:
        start = time.time()
        while time.time() - start < self.timeout:
            for image in images:
                location = self._find_image_on_the_screen(image)
                if location:
                    return location
            time.sleep(self.interval)
        raise TimeoutError(f'Image was not found in {self.timeout} seconds!')

    def _find_image_on_the_screen(self, image: MatLike) -> Coordinates | None:
        screen = self._get_screenshot()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen_gray, image_gray, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= self.threshold)
        if len(locations[0]) < 1:
            return None
        return int(locations[1][0]), int(locations[0][0])
