from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)
led = Pin(25, Pin.OUT)



while True:
    led.value(1)
    gpio_pin.value(1)
    time.sleep(0.5)
    gpio_pin.value(0)
    led.value(0)
    time.sleep(0.5)
