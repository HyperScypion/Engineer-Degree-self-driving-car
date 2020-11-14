import numpy as np
from dataclasses import dataclass


@dataclass
class Box:
    y0: int
    x0: int
    y1: int
    x1: int

    def get_box(self, image: np.ndarray) -> np.ndarray:
        """
        Slices input image to operate only on box selected by user.
        :param image: Image readed and passed as np.ndarray
        :return: Box of image as np.ndarray
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
