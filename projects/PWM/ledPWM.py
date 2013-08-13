import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

pwmpin = 23

gpio.setup(pwmpin, gpio.OUT)

myfirstpwm = gpio.PWM(pwmpin, 100)

myfirstpwm.start(0)

try:

    while True:
        for i in range(100):
            myfirstpwm.ChangeDutyCycle(i)
            time.sleep(0.01)

        for i in range(100):
            myfirstpwm.ChangeDutyCycle(100-i)
            time.sleep(0.01)

    except KeyboardInterrupt:
        pass

myfirstpwm.stop()

gpio.cleanup()