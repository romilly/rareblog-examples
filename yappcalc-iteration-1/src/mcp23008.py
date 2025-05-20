
# MCP23008 registers
_IODIR = const(0x00)
_GPPU  = const(0x06)
_GPIO  = const(0x09)
_OLAT  = const(0x0A)

class MCP23008:
    def __init__(self, i2c, addr=0x20):
        self.i2c = i2c
        self.addr = addr

    def write_reg(self, reg, val):
        self.i2c.writeto_mem(self.addr, reg, bytes([val]))

    def read_reg(self, reg):
        return self.i2c.readfrom_mem(self.addr, reg, 1)[0]

    def setup(self, iodir, pullups):
        # iodir: 1=input, 0=output
        self.write_reg(_IODIR, iodir)
        self.write_reg(_GPPU, pullups)

    def gpio(self, val=None):
        if val is None:
            return self.read_reg(_GPIO)
        else:
            self.write_reg(_OLAT, val)