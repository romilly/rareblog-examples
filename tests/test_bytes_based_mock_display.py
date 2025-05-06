import pytest
from plotting.display import Pen
from plotting.mock_display import BytesBasedMockDisplay

@pytest.fixture
def display():
    """Fixture to create and return a BytesBasedMockDisplay instance."""
    return BytesBasedMockDisplay(480, 320)

def test_can_create_pen(display):
    pen = display.create_pen(0, 128, 255)
    assert isinstance(pen, Pen)
    assert pen.r == 0
    assert pen.g == 128
    assert pen.b == 255

def test_can_create_pen_hsv(display):
    pen = display.create_pen_hsv(0, 1, 1)
    assert pen.r == 255
    assert pen.g == 0
    assert pen.b == 0

def test_can_set_pen(display):
    pen = display.create_pen(0, 128, 255)
    display.set_pen(pen)
    assert display._pen == pen

def test_knows_its_bounds(display):
    assert display.get_bounds() == (480, 320)

def test_knows_its_pixels(display):
    assert display.get_pixel(0, 0) == Pen(0, 0 ,0)
    assert display.get_pixel(479, 319) == Pen(0, 0 ,0)

def test_can_set_pixel(display):
    pen = display.create_pen(0, 128, 255)
    display.set_pen(pen)
    display.pixel(7, 9)
    assert display.get_pixel(0, 0) == Pen(0, 0 ,0)
    assert display.get_pixel(7, 9) == Pen(0, 128 ,255)


