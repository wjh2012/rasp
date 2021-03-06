import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt
import json

import datetime # 시간
import Adafruit_DHT #온도
from RPLCD.i2c import CharLCD #LCD

# 온도 설정
dht_type = 11
bcm_pin = 23
# LCD 설정
lcd = CharLCD('PCF8574', 0x27)

# 세팅
GPIO.setwarnings(False)
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

# Define Variables
MQTT_HOST = "test.mosquitto.org" #자신의 pc ip
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "/CCL/IoTP-UP"

def on_publish(client, userdata, mid):
    print ("Message Published...")

def on_connect ( client, userdata , flags, rc ):
    print("Connect with result code" + str (rc))
    client.subscribe("/CCL/IoTP-DN")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    if msg.payload.decode('utf-8') == "on-201636008":        
        print("good!")

        GPIO.output(16,True)
        GPIO.output(20,True)
        GPIO.output(21,True)

        GPIO.output(13,True)
        GPIO.output(19,True)
        GPIO.output(26,True)

        time.sleep(2)

        GPIO.output(16,False)
        GPIO.output(20,False)
        GPIO.output(21,False)

        GPIO.output(13,False)
        GPIO.output(19,False)
        GPIO.output(26,False)

        data2 = "LED-201636008"
        client.publish(MQTT_TOPIC, data2)

# Initiate MQTT Client
client = mqtt.Client()

# Register publish callback function
client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message

# Connect with MQTT Broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()

try:
    while True:
        # 시간
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        print(nowTime)

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

        if GPIO.input(12)==False:
            data = {'time' : now.strftime('%H:%M:%S'), 'info' : "201636008WJH"}
            client.publish(MQTT_TOPIC, str(data))
            print('Published. Sleeping ...')
        else:
            print('Failed to get reading. Skipping ...')


except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()