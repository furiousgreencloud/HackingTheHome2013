# IMPORTS
from time import sleep
import RPi.GPIO as GPIO

# VARIABLES
pinNo = 25
     
# SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNo, GPIO.OUT)


def main() :
	# LOOP
	while True:
		GPIO.output(pinNo, GPIO.HIGH)
		print("hi")
		sleep(2)
		GPIO.output(pinNo, GPIO.LOW)
		print("lo")
		sleep(1)
		
try :
	main()
finally:
	print("Cleaning Up")
	GPIO.cleanup()
