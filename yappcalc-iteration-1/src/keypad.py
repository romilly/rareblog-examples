from machine import I2C, Pin
import time

from mcp23008 import MCP23008

# Pin assignment
ROW_PINS = [3, 2, 1, 0]     # GPA3–GP1
COL_PINS = [7, 6, 5, 4]     # GPA7–GP4

KEY_MAP = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# init I2C & expander
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
mcp23008 = MCP23008(i2c, addr=0x20)

# set rows=input (0), cols=output (1)
mcp23008.setup(iodir=0b11110000, pullups=0b11110000)

def scan_once():
    """Return first detected keypress or None (no debounce)."""
    for ri, rp in enumerate(ROW_PINS):
        # drive all rows high, then pull this one low
        mask = sum(1 << r for r in ROW_PINS)
        mask &= ~(1 << rp)
        mcp23008.gpio(mask)
        time.sleep_us(100)    # let lines settle
        # check columns
        gv = mcp23008.gpio()
        for ci, cp in enumerate(COL_PINS):
            if not (gv & (1 << cp)):
                return KEY_MAP[ri][ci]
    return None

def scan_debounced():
    """Debounce: accept a key only if it’s stable for 20 ms."""
    first = scan_once()
    if first is None:
        return None
    time.sleep_ms(20)
    second = scan_once()
    return first if first == second else None

# Main loop
last = None
while True:
    key = scan_debounced()
    if key and key != last:
        print("Pressed:", key)
        last = key
    elif key is None:
        last = None
    time.sleep_ms(50)