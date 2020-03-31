import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import picamera
from time import sleep

ip_address = "test.mosquitto.org"  #Write Server IP Address
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
    topic = "cambia_critters"
    f=open("image_test.jpg", "rb") #3.7kiB in same folder
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    client.publish(topic, byteArr)
    print("image published")

def on_message(client, userdata, msg):
    print("message receieved")
    take_picture()
    publish_image()

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883)
client.subscribe("cambia_critters")
client.message_callback_add("cambia_critters", on_message)
#client.on_message = on_message

client.loop_forever()
