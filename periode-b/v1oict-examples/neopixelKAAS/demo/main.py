import time

import machine,neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

while True:
    np[0] = [255, 0, 0]
    np[1] = [0, 255, 0]
    np[2] = [0, 0, 255]
    print(np)
    np.write()

    time.sleep(1)