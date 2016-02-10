from belleds import Belleds
from time import sleep

b = Belleds()
b.connect('172.16.0.1')

lights = b.get_lights()

tweet = " on red"

#print(b.dispatch_cmd())

#powered = 0

# 1st light in series is the lower one, second is back one

for light in lights:

    light.brightness = 200


class StringManip:

    def colorCheck(self):

        tweet = " on red"
        
        if "red" in tweet:
            print("Red")
            #light.color = (255, 0, 0)
            #continue
            sleep(.1)

        if "blue" in tweet:
            print("Blue")
            #light.color = (0, 0, 255)
            #continue
            sleep(.1)

        if "green" in tweet:
            print("Green")
            #light.color = (0, 255, 0)
            #continue
            sleep(.1)

##        if "on" in tweet:
##            powered = 1
##
##        if "off" in tweet:
##            powered = 0

##    if powered == 1:
##        light.brightness = 255
##    else:
##        light.brightness = 255

#    print(powered)
