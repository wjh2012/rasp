import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#LED dictionary
led = {16:False, 20:False, 21:False}

#LED dictionary GPIO.setup
for i in led.keys():
    GPIO.setup(i,GPIO.OUT)

try:
    while True:
        k = input()
        
        if k == 'r':
            led[16] = not led.get(16)
        elif k == 'g':
            led[20] = not led.get(20)
        elif k == 'b':
            led[21] = not led.get(21)
            
        for key, val in led.items():
            GPIO.output(key,val)
            
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()



