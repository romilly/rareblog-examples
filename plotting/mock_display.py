from typing import Tuple

from plotting.display import Display, Pen
from plotting.matrix import Matrix


class BytesBasedMockDisplay(Display):
    def __init__(self, width: int, height: int):
        Display.__init__(self)
        self._width = width
        self._height = height
        self._pixels = Matrix(width, height)

    def get_bounds(self) -> Tuple[int, int]:
        return self._width, self._height

    def create_pen(self, r: int, g: int, b: int):
        return Pen(r, g, b)

    def get_pixel(self, x: int, y: int) -> Pen:
        return self._pixels[x, y]
