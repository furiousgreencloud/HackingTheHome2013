# How to detect a button press without polling the input, using an interrupt

# This version modified to work with my installed RPi.GPIO
# -- no bouncetime
# -- no channel

import RPi.GPIO as GPIO
import os	
import time


GPIO.setmode(GPIO.BOARD)

button = 22 # Wire PIN 22 to a pushbutton so that it will be grounded out when pressed

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#####################################################################################################
# This part defines a FUNCTION (actually a special kind of function called an event handler)...

def button_pressed() :
	print 'I just noticed that you pressed my button and dropped what I was doing to investigate'

#####################################################################################################



GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed)
# ... and this line says to call the function we defined when a falling edge is detected on the button input

# The 'program proper' starts here

print 'Ready'
while(True) :
	# you can do anything you like now, like updating a display or serving web pages,
	# because you don't have to keep checking if the button is pressed
	# but we are lazy so we are just going to have another snooze...

	time.sleep(1)

GPIO.cleanup()
