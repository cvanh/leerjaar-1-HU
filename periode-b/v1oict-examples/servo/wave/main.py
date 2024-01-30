from machine import PWM,Pin
import time

servo_pin = PWM(Pin(21))
servo_pin.freq(100)


def pulse(delay1, delay2 ):
    """ kopier hier je implementatie van de pulse functie """
    servo_pin.duty_u16(1000)
    time.sleep(delay1)
    servo_pin.duty_u16(22000)
    time.sleep(delay2)


def servo_pulse(position):
    """
    Send a servo pulse on the specified gpio pin
    that causes the servo to turn to the specified position, and
    then waits 20 ms.

    The position must be in the range 0 .. 100.
    For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

    Before this function is called,
    the gpio pin must be configured as output.
    """
    position = position * 355
    print(position)
    servo_pin.duty_u16(position)
    time.sleep(0.2)
    #pulse(0.01,0.01)

while True:
    for i in range(0, 100, 1):
        servo_pulse(i)
    for i in range(100, 0, -1):
        servo_pulse(i)