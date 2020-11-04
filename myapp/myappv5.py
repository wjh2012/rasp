import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

GPIO.setup(25,GPIO.IN)
GPIO.setup(25,GPIO.OUT)

GPIO.setup(24,GPIO.IN) #PIR

GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP) #btn
#LED dictionary
led = {16:False, 20:False, 21:False}

#LED dictionary GPIO.setup
for i in led.keys():
    GPIO.setup(i,GPIO.OUT)

# Blink
def blink(x):
    while x==True:
        try:
            for key, val in led.items():
                if val == True:
                    GPIO.output(key,False)
                    
            time.sleep(0.2)
            
            for key, val in led.items():
                if val == True:
                    GPIO.output(key,True)
                
            time.sleep(0.2)
            
        except KeyboardInterrupt:            
            for key in led.keys():
                    GPIO.output(key,False)
                    led[key]=False            
            break

# Moderation
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

m=False
x=False

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
            GPIO.output(20, led[20])
        # B on/off
        elif k == 'b':
            led[21] = not led.get(21)
            GPIO.output(21, led[21])
        
        elif k == 'o':
            for key in led.keys():
                    GPIO.output(key,False)
                    led[key]=False
               
        elif k == 'm':
            t1 = Thread(target=pwm, args=(not m,))
            t1.daemon = True
            t1.start()
        
        elif k == 'x':
            t2 = Thread(target=blink, args=(not x,))
            t2.daemon = True
            t2.start()
            
        elif k == 's':
            for i in range(5):
                buzz()
                time.sleep(0.5)
        
        elif k == 'p':
            while(True):
                if GPIO.input(24)==True:
                    print("SENSOR ON!!")            
                    GPIO.output(16, True)
                    time.sleep(3)
                    GPIO.output(16, False)
                    
                time.sleep(0.5)
        
        elif k == 'o':
            while(True):
                if GPIO.input(12)==True:
                    for i in range(5):
                        buzz()
                        time.sleep(0.5)
                time.sleep(0.5)
                
                print('button pressed')
# OFF
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()




