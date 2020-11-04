import RPi.GPIO as GPIO
import time

import datetime # 시간
import Adafruit_DHT #온도
from RPLCD.i2c import CharLCD #LCD

import picamera #카메라

# 온도 설정
dht_type = 11
bcm_pin = 23
# LCD 설정
lcd = CharLCD('PCF8574', 0x27)
# 카메라 설정
camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT) # LED Blue 1
GPIO.setup(26,GPIO.OUT) # LED Blue 2
GPIO.setup(24,GPIO.IN) # pir sensor
GPIO.setup(25,GPIO.IN) #buzz
GPIO.setup(25,GPIO.OUT) #buzz
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP) #BUTTON

def alarm():
    print("SENSOR ON!!!")
    
    lcd.clear()
    lcd.cursor_pos = (0,3)
    lcd.write_string('Won JangHo')
    lcd.cursor_pos = (1,3)
    lcd.write_string('201636008')
    
    camera.capture('example2.jpg')
    
    
    while True:        
        GPIO.output(26,False)
        GPIO.output(21,True)
        GPIO.output(25, True)
        time.sleep(0.5)
        
        GPIO.output(21,False)
        GPIO.output(26,True)
        GPIO.output(25, False)
        time.sleep(0.5)
        
        if GPIO.input(12)==False:
            GPIO.output(21,False)
            GPIO.output(26,False)
            GPIO.output(25,False)
            break

try:
    while True:        
        GPIO.output(21,False)
        GPIO.output(25,False)
        GPIO.output(26,False)
        # 시간
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        print(now, nowDate, nowTime)
        
        # 온도
        humidity, temperature = Adafruit_DHT.read_retry(dht_type, bcm_pin)
        temp = str(round(temperature,1))
        print(temp)
        
        # 시간표시
        lcd.clear()
        lcd.cursor_pos = (0,3)
        lcd.write_string(nowDate)
        lcd.crlf()
        lcd.cursor_pos = (1,0)
        lcd.write_string(nowTime)
        
        # 온도표시
        lcd.cursor_pos = (1,10)
        lcd.write_string(temp)
        lcd.write_string('C ')
        
        
        if GPIO.input(24) == True:
            alarm()
                 
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
    
        