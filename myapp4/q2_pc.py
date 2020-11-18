import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

normal_temp = 24.0 #원하는 온도 설정
MQTT_Broker = "test.mosquitto.org" #자신의 pc(broker) ip

def on_connect(client, userdata , flags, rc):
    print("Connect with result code" + str(rc) )
    client.subscribe("/CCL/IoTP-UP") #Topic

def on_message(client, userdata , msg) :
    x = str(msg.payload.decode('utf-8')) #rasp 데이터
    print(msg.topic + " " + x)
    if(x!= "LED-201636008"):
        y = eval(x) #rasp 데이터를 Dic타입으로 변환 파싱
        
        if y["info"] == "201636008WJH":
            publish.single("/CCL/IoTP-DN", "on-201636008",hostname = MQTT_Broker)

def on_publish(client, userdata, mid):
    print("message publish..")

def on_disconnect(client, userdata, rc):
    print("Disconnected")

client = mqtt.Client ()
client.on_connect = on_connect
client.connect(MQTT_Broker, 1883, 60)
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.loop_forever()