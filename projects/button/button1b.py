# Reading an input by polling
# Basically this program keeps asking "are we there yet?"
# It's crude but it works!

# This version is a bit different - it has nested loops
# This allows us to do something just ONCE each time the button is pressed.

import RPi.GPIO as gpio
import time

button = 22

gpio.setmode(gpio.BOARD)

gpio.setup(button,gpio.IN,pull_up_down=gpio.PUD_UP)

while 1:
	
	while gpio.input(button) == 1:
		time.sleep(0.01)
		
	# the button has been pushed,now take some action!
	print 'Hey! I was sleeping'

	while gpio.input(button) == 0:
		time.sleep(0.01)
		
	# the button has now been released, so take a different action now if you want.
	print "Thanks - that's better"
	
gpio.cleanup()
