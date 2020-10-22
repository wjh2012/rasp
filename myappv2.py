import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT) #R
GPIO.setup(20,GPIO.OUT) #G
GPIO.setup(21,GPIO.OUT) #B

led = [16,20,21]
led_val = [False, False, False]

def pwm(l_v):
    pwm_led = []
    for i, val in enumerate(l_v):
        if val == True:
            pwm_led[i]= GPIO.PWM(led[i],500)
            pwm_led[i].start(0)
    
            while True:
                for j in range(101):
                    if(j==100):
                        j=0
                    pwm_led[i].ChangeDutyCycle(j)

m = False

try:
    while True:
        key = input()
        
        if key == 'r':
            led_val[0] = not led_val[0]
        elif key == 'g':
            led_val[1] = not led_val[1]
        elif key == 'b':
            led_val[2] = not led_val[2]
        
        for i, channel in enumerate(led):
            GPIO.output(channel,led_val[i])
        
        if key == 'm':
            if m == False:
                pwm(led_val)
                m = True

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()


