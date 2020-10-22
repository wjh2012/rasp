import RPi.GPIO as GPIO
import time

from threading import Thread

GPIO.setmode(GPIO.BCM)

#LED dictionary
led = {16:False, 20:False, 21:False}

#LED dictionary GPIO.setup
for i in led.keys():
    GPIO.setup(i,GPIO.OUT)

def blink(x):    
    while x==True:
        for key, val in led.items():
            if val == True:
                GPIO.output(key,False)
                    
        time.sleep(0.2)
            
        for key, val in led.items():
            if val == True:
                GPIO.output(key,True)
            
        time.sleep(0.2)

def pwm(m):
    for key in led.keys():
        GPIO.output(key,False)
            
    pwm_r = GPIO.PWM(16,500)
    pwm_r.start(0)

    pwm_g = GPIO.PWM(20,500)
    pwm_g.start(0)

    pwm_b = GPIO.PWM(21,500)
    pwm_b.start(0)
    
    while m==True:
        try:
            for i in range(101):
                if(i==100):
                    i=0
                    
                if led[16] == True:
                    pwm_r.ChangeDutyCycle(i)
                    
                if led[20] == True:
                    pwm_g.ChangeDutyCycle(i)
                    
                if led[21] == True:
                    pwm_b.ChangeDutyCycle(i)
            
                time.sleep(0.02)
        
        except KeyboardInterrupt:
            pwm_r.ChangeDutyCycle(0)
            pwm_g.ChangeDutyCycle(0)
            pwm_b.ChangeDutyCycle(0)
            
            for key in led.keys():
                led[key]=False
            
            break

m=False
x=False

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
        
        if k == 'm':
            t1 = Thread(target=pwm, args=(not m))
            t1.daemon = True
            t1.start()
        
        if k == 'x':
            t2 = Thread(target=blink, args=(not x))
            t2.daemon = True
            t2.start()
            
        
            
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()




