from machine import Pin, I2C
from sh1107 import SH1107_I2C

i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
display = SH1107_I2C(128, 128, i2c0, address=0x3c)



class LinePlot:
    def __init__(self):
        i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
        self.display = SH1107_I2C(128, 128, i2c0, address=0x3c)
        self.display.sleep(False)
        self.display.fill(0)
        self.display.show()
        self.width = 128
        self.height = 128
        self.text_margin = 10
        self.frame = Frame(self.width, self.height, 10, 20, 10, 10)

    def display_pixel(self, x, y):
        self.display.pixel(x, y)

    def text(self, x, y, text):
        self.display.text(text, round(x), round(y))

    def blk(self):
        self.display.sleep(False)
        self.display.fill(0)
        self.display.show()

    def line(self, x1, y1, x2, y2):
        self.display.line(x1, y1, x2, y2, 1)

    def add_axes(self):
        self.line(self.frame.left_margin, self.frame.top_margin, self.frame.left_margin, self.frame.bottom())
        self.line(self.frame.left_margin, self.frame.bottom(), self.frame.right(), self.frame.bottom())

    def add_title(self, title: str):
        self.text(self.frame.left_margin - self.text_margin, self.frame.top_margin - self.text_margin, title)

    def show(self):
        self.display.show()

    def plot(self, data, title):
        x_max = max(x for (x, y) in data)
        x_min = min(x for (x, y) in data)
        y_max = max(y for (x, y) in data)
        y_min = min(y for (x, y) in data)
        self.add_axes()
        self.add_title(title)
        scale_x = Scale(x_min, x_max, self.frame.left_margin, self.frame.right())
        scale_y = Scale(y_min, y_max, self.frame.bottom(), self.frame.top_margin + self.text_margin)
        old_x, old_y = data[0]
        for new_x, new_y in data[1:]:
            x1 = scale_x.scale(old_x)
            y1 = scale_y.scale(old_y)
            x2 = scale_x.scale(new_x)
            y2 = scale_y.scale(new_y)
            self.line(x1, y1, x2, y2)
            old_x, old_y = new_x, new_y
        self.show()

class Frame:
    def __init__(self, width, height, top_margin, bottom_margin, left_margin, right_margin):
        self.width  = width
        self.height  = height
        self.top_margin = top_margin
        self.bottom_margin = bottom_margin
        self.left_margin =left_margin
        self.right_margin = right_margin

    def bottom(self):
        return self.height - self.bottom_margin

    def right(self):
        return self.width - self.right_margin

class Scale:
    def __init__(self, d_min, d_max, o_min, o_max):
        self.d_min = d_min
        self.d_max = d_max
        self.o_min = o_min
        self.o_max = o_max
        self.d_range = d_max - d_min
        self.o_range = o_max - o_min
        self.c = self.o_range / self.d_range

    def scale(self, val):
        return round(self.o_min + self.c * (val - self.d_min))






