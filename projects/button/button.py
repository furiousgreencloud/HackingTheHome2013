# Button Press Plays Sound

# from:
# http://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/overview
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3


import RPi.GPIO as GPIO
import os	
from time import sleep as sleep


GPIO.setmode(GPIO.BCM)

buttonPin = 22 # Wire PIN 22 to that it will be grounded out when pressed

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def callback_printYes(channel) :
	print("Yes on Channel: " + str(channel))
	os.system("mpg321 Crow.mp3 &")

GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=callback_printYes, bouncetime=250)


print("Ready")
while(True) :
	# do something way more interesting, like updating a display
	sleep(1)

GPIO.cleanup()
