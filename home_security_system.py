import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT) # LED
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP) #BUTTON
GPIO.setup(24,GPIO.IN) #PIR
GPIO.setup(25,GPIO.IN) #BUZZ
GPIO.setup(25,GPIO.OUT) #BUZZ

control = False

def buzz():
    pitch = 1000
    duration = 0.1
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    
    for i in range(cycles):
        GPIO.output(25, True)
        time.sleep(delay)
        GPIO.output(25, False)
        time.sleep(delay)
        
try:
    while True:
        if GPIO.input(24)==True:
            print("SENSOR ON!!")
            control = True
            
        if control == True:
            while True:
                buzz()
                GPIO.output(16, True)
                
                if GPIO.input(12)==False:
                    GPIO.output(16, False)
                    control = False
                    break                
                time.sleep(0.3)                
        time.sleep(0.3)
        
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()