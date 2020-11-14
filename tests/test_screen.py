import numpy as np
from autopilot.screen import ROI


def test_roi():
    slice = (1, 2, 3, 4)
    image = np.zeros((3, 4))
    roi = ROI(*slice)
    assert roi.get_roi(image).shape == (1, 3)
