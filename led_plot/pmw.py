from machine import Pin, PWM, ADC
from time import sleep

# PWM setup on GPIO15 (can change to another pin if needed)
pwm_pin = PWM(Pin(15))
pwm_pin.freq(100000)  # Set PWM frequency to 100 kHz

# Initialize analog-to-digital converters
adc0 = ADC(0)  # ADC0 used to measure voltage across resistor
adc1 = ADC(1)  # ADC1 used to measure LED voltage

# Number of samples to average for each measurement
SAMPLES = 20

def volts(raw):
    """Convert raw ADC value to voltage in volts
    
    Args:
        raw: Raw 16-bit ADC reading (0-65535)
        
    Returns:
        Voltage in volts (0-3.3V range)
    """
    return raw * (3.3 / 65535)

def read(adc):
    """Take multiple ADC readings and return the average
    
    Args:
        adc: ADC object to read from
        
    Returns:
        Average voltage in volts from SAMPLES readings
    """
    values = SAMPLES*[0.0]
    for i in range(SAMPLES):
        values[i] = volts(adc.read_u16())
        sleep(0.01)  # Small delay between readings
    return sum(values)/SAMPLES


# 16-bit duty cycle (0 to 65535)
def set_analog_voltage(voltsX10):
    """Set PWM duty cycle to generate desired voltage
    
    Args:
        voltsX10: Desired voltage multiplied by 10 (e.g., 33 = 3.3V)
        
    Returns:
        The actual duty cycle value set (0-65535)
    """
    duty = int((voltsX10 / 33.0 ) * 65535)
    pwm_pin.duty_u16(duty)
    return duty

# Print header for measurement results
print(' Vl,     mA')

# Sweep through different voltage levels
for i in range(10, 34, 2):  # From 1.0V to 3.3V in 0.2V steps
    # Set the PWM to the desired voltage
    duty = set_analog_voltage(i)
    
    # Allow time for the circuit to stabilize
    sleep(0.3)
    
    # Take measurements
    v_res = read(adc0)  # Voltage across resistor
    v_led = read(adc1)  # Voltage across LED
    
    # Calculate voltage difference and current
    v_diff = v_led - v_res
    mA = 10 * v_diff  # Current in milliamps (assuming 100 ohm resistor)
    
    # Print measurement results
    print(f'{v_led:.2f}, {mA:>5.2f}')