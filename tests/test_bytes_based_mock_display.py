from plotting.display import Display


class Pen:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b


class BytesBasedMockDisplay(Display):
    def create_pen(self, r: int, g: int, b: int):
        return Pen(r, g, b)


def test_can_create_pen():
    display = BytesBasedMockDisplay()
    pen = display.create_pen(0, 128, 255)
    assert isinstance(pen, Pen)
    assert pen.r == 0
    assert pen.g == 128
    assert pen.b == 255