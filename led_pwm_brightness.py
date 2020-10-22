import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

pwm_led = GPIO.PWM(16, 500)
pwm_led.start(0)

try:
    while True:
        for i in range(101):
            if(i==100):
                i=0
            pwm_led.ChangeDutyCycle(i)
            time.sleep(0.02)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
