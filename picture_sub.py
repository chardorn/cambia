import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print("Connect" + str(rc))
    client.subscribe("image")

def on_message(client, userdata, msg):
    print("Topic : ", msg.topic)
    f = open("/tmp/output.jpg", "w")  #there is a output.jpg which is different
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.connect("192.168.43.191")
client.on_connect = on_connect
client.on_message = on_message

#client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
