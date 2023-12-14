from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)

def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.high()
    time.sleep(high_time)
    pin.low()
    time.sleep(low_time)


def morse(pin, dot_length, text):
    """
    Laat de text horen als morse code.
    De pin is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """
    # loop trough the charachter and decide what pulse to give
    for char in text:
        if char == ".":
            pulse(pin, dot_length, 1)
        if char == "-":
            pulse(pin, dot_length * 4, 1)
        if char == " ":
            pulse(pin, dot_length * 7, 0)

        # space 1 unit behind everything
        pulse(pin, dot_length, 1)
        

morse(gpio_pin, 0.2, ".--. -.-- - .... --- -.")
