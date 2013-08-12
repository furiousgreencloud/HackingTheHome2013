# IMPORTS
from time import sleep
import RPi.GPIO as GPIO
     
# SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)


while True: # loop forever
	GPIO.output(25, GPIO.HIGH) #make pin 25, go into a HIGH voltage state
	print("HIGH") #print out the text "HIGH"
	sleep(2) # sleep for 2 seconds
	GPIO.output(25, GPIO.LOW)
	print("LOW")
	sleep(1)

GPIO.cleanup()
