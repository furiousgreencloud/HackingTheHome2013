# How to detect a button press without polling the input, using an interrupt

# modified from 'button.py':
#	-- python 2 print statements
#	-- commented


import RPi.GPIO as GPIO
import os	
import time


GPIO.setmode(GPIO.BOARD)

button = 22 # Wire PIN 22 so that it will be grounded out when pressed

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#####################################################################################################

# This part defines a FUNCTION (actually a special kind of function called an event handler)...

def button_pressed(channel) :
	print 'I just noticed that you pressed my button and dropped what I was doing to investigate'

#####################################################################################################



GPIO.add_event_detect(button, GPIO.FALLING, callback=button_pressed, bouncetime=250)

# ... and this line says to run the function we defined when a falling edge is detected on the button input

# The 'program proper' starts here

print 'Ready'
while(True) :
	# you can do anything you like now, like updating a display or serving web pages,
	# because you don't have to keep checking if the button is pushed.
	# but we are lazy so we are just going to have another snooze...

	time.sleep(1)

GPIO.cleanup()
