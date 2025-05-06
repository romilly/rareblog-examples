from plotting.display import Display, Pen


class BytesBasedMockDisplay(Display):
    def create_pen(self, r: int, g: int, b: int):
        return Pen(r, g, b)
