import RPi.GPIO as GPIO
import time
from threading import Thread

import blink
import pwm

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #R
GPIO.setup(20,GPIO.OUT) #G
GPIO.setup(21,GPIO.OUT) #B

# LED dictionary state
led = {16:False, 20:False, 21:False}

# pwm state
m = False

# blink state
x = False

try:
    while True:
        k = input()
        
        # R on/off
        if k == 'r':
            led[16] = not led.get(16)
            GPIO.output(16, led[16])
        # G on/off
        elif k == 'g':
            led[20] = not led.get(20)
            GPIO.output(16, led[16])
        # B on/off
        elif k == 'b':
            led[21] = not led.get(21)
            GPIO.output(16, led[16])
        
        # pwm moderation
        elif k == 'm':
            t1 = Thread(target=pwm, args=(not m))
            t1.daemon = True
            t1.start()
        
        # blink
        elif k == 'x':
            t2 = Thread(target=blink, args=(not x))
            t2.daemon = True
            t2.start()

# OFF
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
