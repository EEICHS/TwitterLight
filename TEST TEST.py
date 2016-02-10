from belleds import Belleds
from time import sleep
from STRING_MANIPULATION import StringManip

b = Belleds()
b.connect('192.168.11.7')

lights = b.get_lights()
sM = StringManip()

tweet = " on red"


#powered = 0

# 1st light in series is the lower one, second is back one

for light in lights:

    light.brightness = 10

    lightValue = sM.colorCheck()

    while lightValue != None: #for whatever reason, the CC returns "None"
        print(lightValue)
        break
