# Reading an input by polling
# Basically this program keeps asking "are we there yet?"
# It's crude but it works!

import RPi.GPIO as gpio
import time

button = 22
output_pin = 12

gpio.setmode(gpio.BOARD)

gpio.setup(button,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(output_pin,gpio.OUT,initial=0)

while 1:
	
	time.sleep(0.5)
	
	if gpio.input(button) == 0:
	
		print 'Hey! I was sleeping'
		gpio.output(output_pin,1)
		
#	else:
		
		# do something else
		