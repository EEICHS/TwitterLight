from belleds import Belleds
from time import sleep



#tweet = " on blue"

#print(b.dispatch_cmd())

#powered = 0

# 1st light in series is the lower one, second is back one

b = Belleds()
b.connect('172.16.0.1')
lights = b.get_lights()


class StringManip:

    def colorCheck(self, the_tweet):

        the_tweet = the_tweet.lower()

        print("Function called.")
        
        #tweet = " on red"

        for light in lights: #basic iterator, reset to lights

            light.brightness = 250

            print("Setting light...")

            if "white" in the_tweet:
                print("White")
                light.color = (255, 255, 255)
                #continue
                sleep(0.15)
                #return white
                
            elif "red" in the_tweet:
                print("Red")
                light.color = (255, 0, 0)
                #continue
                sleep(0.15)
                #return red

            elif "blue" in the_tweet:
                print("Blue")
                light.color = (0, 0, 255)
                #continue
                sleep(0.15)
                #return "blue"

            elif "green" in the_tweet:
                print("Green")
                light.color = (0, 255, 0)
                #continue
                sleep(0.15)
                #return "green"

            elif "purple" in the_tweet:
                print("Purple")
                light.color = (127, 0, 127)
                #continue
                sleep(0.15)
                #return "purple"

            elif "navy" in the_tweet:
                print("Navy")
                light.color = (5, 0, 70)
                #continue
                sleep(0.15)
                #return "navy"

            elif "yellow" in the_tweet:
                print("Yellow")
                light.color = '#FFFF00'
                #continue
                sleep(0.15)
                #return "yellow"

            elif "maroon" in the_tweet:
                print("Maroon")
                light.color = (130, 0, 0)
                #continue
                sleep(0.15)
                #return "yellow"

##            sM.colorCheck()




        

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
