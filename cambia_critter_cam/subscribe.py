import paho.mqtt.client as mqtt
import subprocess

ip_address = "test.mosquitto.org"
topic = "cambia_critters"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)
    # The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    # Create a file with write byte permission
    f = open('output.jpg', "wb")
    f.write(msg.payload)
    print("Image Received")
    f.close()
    openimg = subprocess.call(["open", "output.jpg"])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
