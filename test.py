import paho.mqtt.client as mqtt
import time

def messageFunction (client, userdata, message):
	topic = str(message.topic)
	message = str(message.payload.decode("utf-8"))
	print(topic + message)

ourClient = mqtt.Client("makerio_mqtt")
ourClient.connect("192.168.43.191")
ourClient.subscribe("testy")
ourClient.on_message = messageFunction
ourClient.loop_start()

while(1):
	ourClient.publish("testy", "hubbala")
	time.sleep(1)
