import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

count = 0
while True:
    # increment and change each light
    for i in range(7):
      k = [0,0,0]  
      k[count] = 255
      
      np[i] = k

      time.sleep(1)
      np.write()
    
    count = count + 1

    # turn leds of
    np.fill((0,0,0))
    time.sleep(1)

    # if we looped 3 times we exit
    if count == 3:
      break

