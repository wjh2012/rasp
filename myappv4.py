import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#LED dictionary
led = {16:False, 20:False, 21:False}

#LED dictionary GPIO.setup
for j in led.keys():
    GPIO.setup(j,GPIO.OUT)

pwm_r = GPIO.PWM(16,500)
pwm_r.start(0)

pwm_g = GPIO.PWM(20,500)
pwm_g.start(0)

pwm_b = GPIO.PWM(21,500)
pwm_b.start(0)

def pwm():
    while True:
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
        
try:
    while True:
        k = input()
        
        if k == 'r':
            if led[16]:
                led[16]=False
                pwm_r.ChangeDutyCycle(0)
            else:   
                pwm_r.ChangeDutyCycle(100)
                led[16]=True
            
        elif k == 'g':
            if led[20]:
                led[20]=False
                pwm_g.ChangeDutyCycle(0)
            else: 
                pwm_g.ChangeDutyCycle(100)
                led[20]=True
            
        elif k == 'b':
            if led[21]:
                led[21]=False
                pwm_b.ChangeDutyCycle(0)
            else:
                pwm_b.ChangeDutyCycle(100)
                led[21]=True
        
        if k == 'm':
            pwm()
            
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()




