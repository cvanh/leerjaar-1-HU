import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    for i in range(7):
      np[i] = [255,0,0]  
      time.sleep(1)
      np.write()

    # turn leds of
    np.fill((0,0,0))
    time.sleep(1)

