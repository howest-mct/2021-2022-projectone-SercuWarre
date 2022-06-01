import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.HIGH)

# main loop
try:
  GPIO.output(6, GPIO.LOW)
  time.sleep(2);
  GPIO.output(6, GPIO.HIGH)
  time.sleep(2);
  print ("Works")
  GPIO.cleanup()
  print ("Good bye!")
except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        GPIO.cleanup()
finally:
    print("script stopped")