# Hardware Timed Servo/PWM Control

# IMPORTANT: 
# This project requires a custom (currently non Raspbian) kernel with the PWM module
#
# As Detailed at:
#  	http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2
# I install this custome kernel from OccidentalisV02Kernel.tgz, which in included int the /resources folder

import os
from time import sleep

DEBUG = 0
servopath = "/sys/class/rpi-pwm/pwm0"


def quote(s) :
	return '"' + s.replace('"','\\"') + '"'
	
def shell(cmd) :
	if DEBUG : 
		print("Doing: \n\t" + cmd)
	return os.system(cmd)

# REQUIRMENTS CHECK

check = shell("ls " + servopath + "/mode")
if check != 0 :
	print("PWM Kernel Module not installed")
	print("\t" + servopath + ", not found")
	exit(1)

# SETUP
	
shell("echo 180 > " + servopath + "/servo_max")	

def angle(deg) :
	shell("echo " + str(deg) + " " + servopath + "/servo")
	

def main() :
		delay = 0.1
		
		for d in range(0,181) :
			angle(d)
			sleep(delay)
		for d in range(179, 0, -1) :
			angle(d)
			sleep(delay)


try :			
	main()
except KeyboardInterrupt:
	pass
