import paho.mqtt.client as mqtt
import base64
import random, string
import math
import time
import uuid
import json

packet_size=3000

def messageFunction (client, userdata, message):
	topic = str(message.topic)
	message = str(message.payload.decode("utf-8"))
	print(topic + message)

def randomword(length):
    return ''.join(random.choice(uuid.uuid4().hex) for i in range(length))

def convertImageToBase64():
    with open("image_test.jpg", "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
    return encoded

def publishEncodedImage(encoded):
    end = packet_size
    start = 0
    length = len(encoded)
    picId = randomword(8)
    pos = 0
    no_of_packets = math.ceil(length/packet_size)

    while start <= len(encoded):
        data = {"data": encoded[start:end], "pic_id":picId, "pos": pos, "size": no_of_packets}
        ourClient.publish("Image-Data",json.JSONEncoder().encode(data))
        end += packet_size
        start += packet_size
        pos = pos +1

ourClient = mqtt.Client("makerio_mqtt")
ourClient.connect("192.168.43.191")
ourClient.subscribe("testy")
ourClient.on_message = messageFunction
ourClient.loop_start()

encoded = convertImageToBase64()
publishEncodedImage(encoded)
