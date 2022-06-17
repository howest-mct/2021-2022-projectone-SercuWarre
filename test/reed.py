import time, sys
import RPi. GPIO as GPIO
GPIO.setmode (GPIO. BCM)
GPIO.setup (21, GPIO .IN, pull_up_down = GPIO.PUD_UP)
while True:
    input = GPIO.input (21)
    print (input)
    time.sleep (1)