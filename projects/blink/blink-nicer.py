# IMPORTS
from time import sleep
from RPi.GPIO import *

# VARIABLES
pinNo = 25
     
# SETUP
setmode(BCM)
setup(pinNo, OUT)

# MAIN
def main() :
	# Loop Forever
	while True:
		output(pinNo, HIGH)
		print "hi"
		sleep(2)
		output(pinNo, LOW)
		print "lo"
		sleep(1)
		
try :
	main()
except : 
	KeyboardInterrupt
	print "\nCleaning Up"
	cleanup() # 
