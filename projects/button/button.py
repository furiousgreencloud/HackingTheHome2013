import RPi.GPIO as GPIO
from time import sleep as sleep

GPIO.setmode(GPIO.BCM)

buttonPin = 22 # Wire PIN 22 to that it will be grounded out when pressed

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def callback_printYes(channel) :
	print("Yes on Channel: " + str(channel))

GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=callback_printYes, bouncetime=300)


while(True) :
	# do somethign way more interesting, like updating a display
	sleep(1)

