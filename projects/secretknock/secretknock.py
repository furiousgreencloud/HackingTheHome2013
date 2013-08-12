#########################################
# Secret knock decoder for Raspberry Pi #
#     by Simon Lyons, August 2013       #
#########################################

# Please acknowledge authorship if you reuse or re-post this code!
# Visit www.MakerMobile.org and let us know what fun stuff you get up to!

# Connect a switch, piezo disc, amplified electret mic etc to an input pin.
# Note that piezos can produce voltages well outside the supply voltage range of the Pi,
# so I recommend protecting the input with fast diodes (preferably Schottky). Also
# a piezo should be loaded with a resistor of ~1Mohm in parallel for good output.
# Don't use any pullup/down resistors on an input connected to a piezo.
# If using an amplified mic, power the amp from the Pi's 3V3 rail so the output can't
# possibly go too high or low.

# The first time you run the program, make a note of the values that it spits out.
# Then edit the 'pattern' list so it contains your own values.


import time
import RPi.GPIO as gpio

# Variables

sensor = 22
green_led = 18

pattern = [36,18,18,36,72,36] # change this to the values that represent your unique knock.
# The numbers represent hundredths of a second between consecutive knocks.

top = len(pattern) - 1
# Later on in the program we need to know how many values are in the stored pattern.
# The reason for subtracting one is that the list elements are numbered 0, 1, 2 etc.

max = 1.3
min = 0.7
# we have to allow for small variations in timing. The default is to allow times to vary by + or - 30%

blanking_period = 10
# don't bother checking the input again for this many hundredths after a pulse is received
# because we may find the sensor has not settled down yet.

# Setup

# Set input and output pins.
gpio.setmode(gpio.BOARD)
gpio.setup(sensor,gpio.IN,pull_up_down=gpio.PUD_UP) 	# uncomment this line if using a switch 
# gpio.setup(sensor,gpio.IN) 				# uncomment this line if using a piezo sensor
gpio.setup(green_led,gpio.OUT,initial=0)

fails = 0
n = top

while 1:

    if fails > 0 or n < top:
		print 'Failed attempt!'
    fails = 0
    n = 0

    while gpio.input(sensor) == 1:	# wait for the first knock
        time.sleep(0.01)

    print
    print "Hello - what's this..."

    while 1:
        time.sleep(blanking_period / 100.0)
        interval = blanking_period

        while gpio.input(sensor) == 1:	# wait for subsequent knocks
            time.sleep(0.01)
            interval += 1
            if interval >= 200:		# max gap of 2s betweek knocks or it starts over
                break

        if interval >= 200:
            break

        print interval,

        if n <= top:
       

            if interval >= (min * pattern[n]) and interval <= (max * pattern[n]) :
                if n == top and fails == 0 :
		# TURN ON GREEN LED or take other exciting action
                    print "Congratulations...you're in!"
                    gpio.output(green_led,1)
                    time.sleep(1.00)
                    gpio.output(green_led,0)
                    break
            else:
                fails += 1

        n += 1

gpio.cleanup()
