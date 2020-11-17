import paho.mqtt.client as mqtt

mqtt = mqtt.Client("python_pub") #Mqtt Client 오브젝트 생성
mqtt.connect("localhost", 1883) #MQTT 서버에 연결

mqtt.publish("IoT-P", "led on") #토픽과 메세지 발행
mqtt.publish("IoT-P", "led off")

mqtt.loop(2) #timeout 2sec.