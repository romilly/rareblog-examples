from machine import Pin, PWM, ADC
from time import sleep

# PWM setup on GPIO15 (can change to another pin if needed)
pwm_pin = PWM(Pin(15))
pwm_pin.freq(100000)  

adc0 = ADC(0)
adc1 = ADC(1)

SAMPLES = 20
def volts(raw):
    return raw * (3.3 / 65535)

def read(adc):
    values = SAMPLES*[0.0]
    for i in range(SAMPLES):
        values[i] = volts(adc.read_u16())
        sleep(0.01)
    # print(values)
    return sum(values)/SAMPLES


# 16-bit duty cycle (0 to 65535)
def set_analog_voltage(voltsX10):
    """Set PWM duty cycle as a percentage (0–100%)"""
    duty = int((voltsX10 / 33.0 ) * 65535)
    pwm_pin.duty_u16(duty)
    return duty

sleep(5)
print(' Vl,     mA')
for i in range(10, 34, 2):
    duty = set_analog_voltage(i)
    sleep(0.3)
    v_res = read(adc0)
    v_led = read(adc1)
    v_diff = v_led - v_res
    mA = 10 * v_diff
    v_diff = v_led - v_res
    print(f'{v_led:.2f}, {mA:>5.2f}')
