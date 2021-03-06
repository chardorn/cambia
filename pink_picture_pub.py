import paho.mqtt.client as client
import paho.mqtt.publish as publish
import picamera
from time import sleep

ip_address = "192.168.1.191"  #Write Server IP Address
camera = picamera.PiCamera()

def take_picture():
    try:
        camera.start_preview()
        sleep(1)
        camera.capture('image_test.jpg', resize=(500,281))
        camera.stop_preview()
        pass
    finally:
        #camera.close()
        pass

def publish_image():
    topic = "image"
    f=open("image_test.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client.publish("image", byteArr)
    print("image published")

def on_message(client, userdata, msg):
    print("message receieved")
    take_picture()
    publish_image()

client = client.Client()
client.connect("192.168.1.191")
client.subscribe("request")
client.message_callback_add("request", on_message)
#client.on_message = on_message

client.loop_forever()
