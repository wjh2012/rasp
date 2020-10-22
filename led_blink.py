import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

try:
    while True:
        GPIO.output(16,True)
        time.sleep(0.1)
        GPIO.output(16,False)
        time.sleep(0.1)
        GPIO.output(20,True)
        time.sleep(0.1)
        GPIO.output(20,False)
        time.sleep(0.1)
        GPIO.output(21,True)
        time.sleep(0.1)
        GPIO.output(21,False)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()