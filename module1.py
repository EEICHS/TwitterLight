#!/usr/bin/env python3

from belleds import Belleds
from time import sleep

b = Belleds()
b.connect('192.168.11.8')

l = b.get_lights()

#lights = b.get_lights()

for light in l:
    for i in range(0, 255):
        light.brightness = i
        sleep(.01)