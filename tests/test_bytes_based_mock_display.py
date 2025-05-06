from plotting.display import Pen
from plotting.mock_display import BytesBasedMockDisplay


def test_can_create_pen():
    display = BytesBasedMockDisplay()
    pen = display.create_pen(0, 128, 255)
    assert isinstance(pen, Pen)
    assert pen.r == 0
    assert pen.g == 128
    assert pen.b == 255

def test_can_create_pen_hsv():
    display = BytesBasedMockDisplay()
    pen = display.create_pen_hsv(0, 1, 1)
    assert pen.r == 255
    assert pen.g == 0
    assert pen.b == 0



