from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Tuple


def hsv_to_rgb(h: float, s: float, v: float):
    """
    Convert HSV color to RGB

    Parameters:
    h (float): Hue in degrees (0-360)
    s (float): Saturation (0-1)
    v (float): Value (0-1)

    Returns:
    tuple: (r, g, b) with values in range 0-255
    """
    if s == 0.0:
        # Achromatic (grey)
        return round(v * 255), round(v * 255), round(v * 255)

    h = h / 60  # sector 0 to 5
    i = int(h)
    f = h - i  # factorial part of h
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))

    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:  # i == 5
        r, g, b = v, p, q

    return round(r * 255), round(g * 255), round(b * 255)


@dataclass(frozen=True)
class Pen:
    r: int
    g: int
    b: int

class Display(ABC):
    def __init__(self):
        self._pen = None

    @abstractmethod
    def create_pen(self, r: int, g: int, b: int) -> Pen:
        pass

    def create_pen_hsv(self, h: float, s: float, v: float) -> Pen:
        return Pen(*hsv_to_rgb(h, s, v))

    def set_pen(self, pen: Pen):
        self._pen = pen

    @abstractmethod
    def get_bounds(self) -> Tuple[int, int]:
        pass

    @abstractmethod
    def get_pixel(self, x: int, y: int) -> Pen:
        pass

    @abstractmethod
    def pixel(self, x: int, y: int) -> None:
        pass

