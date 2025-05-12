from machine import Pin, ADC
from time import sleep
from plotter import  LinePlot

SAMPLES = 8

def volts(adc):
    v = SAMPLES*[0.0]
    for i in range(SAMPLES):
        raw = adc.read_u16()
        v[i] = raw * (3.3 / 65535)
    return sum(v)/SAMPLES

adc0 = ADC(0)
adc1 = ADC(1)
resistors =   [10, 15, 22, 33, 56, 82, 100,  120]
pin_numbers = [15, 14, 13, 12, 11, 10,   9,    8]
pins = [Pin(pin_number, mode=Pin.OUT) for pin_number in pin_numbers]

for pin in pins:
    pin.off()
pins[7].on()
sleep(1)

def measure():
    result = []
    for resistor, pin in zip(resistors, pins):
        pin.on()
        sleep(0.1)
        v0 = volts(adc0)
        v1 = volts(adc1)
        voltage = v1 - v0
        current_ma = 100 * voltage
        result.append([resistor + 10, current_ma])
       # print(3.3 - v1, current_ma)
        pin.off()
    return result

def print_values(values):
    print(' Vl,     mA')
    for v_led, mA in values:
        print(f'{v_led:.2f}, {mA:>5.2f}')

def plot(data):
    lp = LinePlot()
    lp.plot(data, 'LED volts vs mA')

values = measure()
print_values(values)
plot(values)







