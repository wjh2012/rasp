import RPi.GPIO as GPIO
import time

import Adafruit_DHT #온도
from RPLCD.i2c import CharLCD #LCD

# 온도 설정
dht_type = 11
bcm_pin = 23
# LCD 설정
lcd = CharLCD('PCF8574', 0x27)

GPIO.setmode(GPIO.BCM)

# LED
GPIO.setup(16,GPIO.OUT) #R
GPIO.setup(20,GPIO.OUT) #G
GPIO.setup(21,GPIO.OUT) #B

GPIO.setup(13,GPIO.OUT) #R
GPIO.setup(19,GPIO.OUT) #G
GPIO.setup(26,GPIO.OUT) #B

# 버튼
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)

control=False

try:
    while True:
        # 온도
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
        temp = str(round(temperature,1))
        print(temp)

        lcd.clear()
        # 온도표시
        lcd.cursor_pos = (0,3)
        lcd.write_string(temp)
        lcd.write_string('C ')
        # 이름표시
        lcd.cursor_pos = (1,3)
        lcd.write_string('Won JangHo')

        button_state=GPIO.input(12)
        if button_state == False:
            
            if(control == True):
                control = False
            else:
                control= True
                
            print('button pressed')
        
        if control == True:
            GPIO.output(16,True)
            GPIO.output(20,True)
            GPIO.output(21,True)

            GPIO.output(13,True)
            GPIO.output(19,True)
            GPIO.output(26,True)

        else:
            GPIO.output(16,False)
            GPIO.output(20,False)
            GPIO.output(21,False)

            GPIO.output(13,False)
            GPIO.output(19,False)
            GPIO.output(26,False)

except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()