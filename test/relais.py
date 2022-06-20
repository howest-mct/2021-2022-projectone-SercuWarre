import RPi.GPIO as GPIO
import time

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)

# main loop

    GPIO.output(6, GPIO.LOW)
    time.sleep(2);
    GPIO.output(6, GPIO.HIGH)
    time.sleep(2);
    print ("Works")
    GPIO.cleanup()
    print ("Good bye!")
