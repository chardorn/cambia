import paho.mqtt.client as mqtt
import base64
import random, string
import math
import time

def on_publish(mosq, userdata, mid):
    mosq.disconnect()

client = mqtt.Client("makerio_mqtt")
client.connect("192.168.43.191")
client.subscribe("image")
client.on_publish = on_publish

f=open("image_test.jpg", "rb") #3.7kiB in same folder
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("image", "here")
client.publish("image",byteArr,0)

client.loop_start()
