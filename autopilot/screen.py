import numpy as np
from mss import mss
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
    def height(self) -> int:
        return self.y1 - self.y0

    @property
    def width(self) -> int:
        return self.x1 - self.x0

    @staticmethod
    def from_tuple(tuple_: tuple):
        return Box(tuple_[0], tuple_[1], tuple_[2], tuple_[3])

    def return_params(self):
        return self.y0, self.x0, self.y1, self.x1


class Monitor:
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    @property
    def to_dict(self):
        return {
            "left": self.left,
            "top": self.top,
            "width": self.width,
            "height": self.height,
        }

    def grab_monitor(self):
        return np.array(mss().grab(self.to_dict))


class Window:
    def __init__(self):
        self.name = ""
        self.width = ""
        self.height = ""

    def from_tuple(self, image):
        raise NotImplementedError

    def from_box(self, box: Box):
        raise NotImplementedError
