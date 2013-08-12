# This example shows how you can launch another program or
# a system command from within aPython program. In this case
# we are using the mpg321 program to play an mp3 file.
# The & sign at the end of the command tells the system not to
# open another terminal window for this program. 

import os

os.system("mpg321 Crow.mp3 &")

