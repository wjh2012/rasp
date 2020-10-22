import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
GPIO.setup(25,GPIO.OUT)

def buzz():
    pitch = 1000
    duration = 0.1
    period = 1.0/pitch
    delay = period/2
    cycles = int(duration * pitch)
    
    for i in range(cycles):
        GPIO.output(25, True)
        time.sleep(delay)
        GPIO.output(25, False)
        time.sleep(delay)
try:
    while True:
        buzz()
        time.sleep(0.5)
    
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()

