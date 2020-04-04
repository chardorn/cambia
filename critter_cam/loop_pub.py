import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import picamera
from time import sleep

ip_address = "test.mosquitto.org"
camera = picamera.PiCamera()
topic = "cambia_critters"


def take_picture():
    try:
        camera.start_preview()
        sleep(1)
        camera.capture('image_test.jpg', resize=(500,281))
        camera.stop_preview()
        pass
    finally:
        pass

def publish_image():
    f=open("image_test.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client.publish(topic, byteArr)
    print("image published")

client = mqtt.Client()
client.connect(ip_address, 1883)
client.subscribe(topic)


while(1):
    sleep(5)
    take_picture()
    publish_image()
