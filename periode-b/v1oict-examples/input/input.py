from machine import Pin
import time

led_pin = Pin(20, Pin.OUT)
off_pin = Pin(19, Pin.IN, pull=Pin.PULL_DOWN)
on_pin = Pin(18, Pin.IN, pull=Pin.PULL_DOWN)

while True:
    # if the on pin is pressed turn the led on
    if on_pin.value():
        led_pin.value(1)

   # if the off pin is pressed turn the led off 
    if off_pin.value():
        led_pin.value(0)
    time.sleep(0.1)
