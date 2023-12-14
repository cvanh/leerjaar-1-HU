from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

def blink(sleeptime):
    gpio_pin.high()
    time.sleep(sleeptime)
    gpio_pin.low()
    time.sleep(sleeptime)

while True:
    blink(0.5)
    blink(0.5)
    blink(0.5)
    blink(1)
