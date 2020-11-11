import numpy as np
from dataclasses import dataclass


@dataclass
class ROI:
    y0: int
    x0: int
    y1: int
    x1: int

    def get_roi(self, image: np.ndarray) -> np.ndarray:
        """
        Method which slice input image to operate only on selected by user part
        :param image: Image readed and passed as np.ndarray
        :return: Sliced image as np.ndarray
        """
        return image[self.x0 : self.x0 + self.x1, self.y0 : self.y0 + self.y1]

    @property
    def height(self):
        return self.y1 - self.y0

    @property
    def width(self):
        return self.x1 - self.x0


class Window:
    def __init__(self):
        pass

    def select_screen(self, image):
        raise NotImplementedError
