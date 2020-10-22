import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

try:
    while True:
        if GPIO.input(24) == True:
            print("SENSOR ON!!!")
            GPIO.output(16,True)
        
        if GPIO.input(24) == False:
            print("SENSOR OFF!!!")
            GPIO.output(16,False)
        
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
