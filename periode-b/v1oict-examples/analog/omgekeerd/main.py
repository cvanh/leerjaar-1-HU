from machine import ADC, PWM, Pin
import time

led = PWM(Pin(20))
led.freq(1000)

adc = ADC(Pin(26))


def led_brightness(value):
    """
        Zet de led intensiteit.
        Waarde tussen de 0 en 65535
    """
    # the max value of a unsigned 16 int
    max_value = 65535
    led.duty_u16(max_value - value)


while True:
    adc_value = adc.read_u16()
    print(adc_value)
    led_brightness(adc_value)
    time.sleep(0.11)

