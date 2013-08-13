# This program takes a command-line argument of a number 0-10
# and sends it to a 7 segment display connected to the specified pins.
# GPIO cleanup is not performed so the output will persist after the program exits.
# 10 means all segments off.

# usage: (a) sudo python 7seg.py 5  (b) sudo python 7seg.py 10
# (a) will display a 5 on the 7-segment display
# (b) will blank the display


import RPi.GPIO as io
import sys

io.setmode(io.BOARD)
io.setwarnings(False)

segment_on = 1
segment_off = 0
# depending on common anode/cathode display

pinmap = [7,11,13,15,19,21,23]
#format: [pin# for seg 1, pin# for seg 2 etc ...]

digit = [[],[],[],[],[],[],[],[],[],[],[]]
# the segments that are illuminated for each digit

try:
	
	for i in pinmap :
		io.setup(i, io.OUT, initial=segment_off)
	#	io.output(i, segment_off)

	for j in digit[int(sys.argv[1])] :
		io.output(pinmap[j-1], segment_on)
	
except:
	
	pass
	
