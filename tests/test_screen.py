import numpy as np
from autopilot.screen import Box


def test_roi():
    slice = (1, 2, 3, 4)
    image = np.zeros((3, 4))
    box = Box(*slice)
    assert box.get_box(image).shape == (1, 3)
