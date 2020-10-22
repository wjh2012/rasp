import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)
control=False

try:
    while True:
        button_state=GPIO.input(12)
        if button_state == False:
            
            if(control == True):
                control = False
            else:
                control= True
                
            print('button pressed')
        
        if control == True:
            GPIO.output(16,True)
        else:
            GPIO.output(16,False)
        
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
