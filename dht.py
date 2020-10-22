import Adafruit_DHT
import time

dht_type = 11
dht_pin = 23

while True:
    
    humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f} C  Humidity={1:0.1f}%'.format(temperature, humidity))
        
    time.sleep(3)