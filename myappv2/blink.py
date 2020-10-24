import RPi.GPIO as GPIO

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