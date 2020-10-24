import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT) #R
GPIO.setup(20,GPIO.OUT) #G
GPIO.setup(21,GPIO.OUT) #B

r=False
g=False
b=False

try:
    while True:        
        a = input()
        
        if a=='r':
            if r==False:
                print("R on")
                GPIO.output(16,True)
                r=True
            else:
                GPIO.output(16,False)
                r=False
                
        elif a=='g':
            if g==False:
                print("G on")
                GPIO.output(20,True)
                g=True
            else:
                GPIO.output(20,False)
                g=False
                
        elif a=='b':
            if b==False:
                print("B on")
                GPIO.output(21,True)
                b=True
            else:
                GPIO.output(21,False)
                b=False
        else:
            pass
        

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()

