#This program should run on a computer or raspberry pi as a backup in case no other internet access is available.

#if there is internet access, send the data to the internet as individual data or in CSVs
#if there is no internet access, store the data is a CSV file

#ARDUINO should send mqtt message to a topic of the name field 1, field 2, etc
#up to 8.

from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook


MQTT_HOST = "localhost"

channels = "field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8"
stored_data = False

excelOut = os.path.join(current_directory, 'SavedData.xlsx')


###   Start of user configuration   ###

#  ThingSpeak Channel Settings

# The ThingSpeak Channel ID
# Replace this with your Channel ID
channelID = "1028998"

# The Write API Key for the channel
# Replace this with your Write API key
apiKey = "6MCNQF4KPLG2D5O8"

#  MQTT Connection Methods

# Set useUnsecuredTCP to True to use the default MQTT port of 1883
# This type of unsecured MQTT connection uses the least amount of system resources.
useUnsecuredTCP = True

# Set useUnsecuredWebSockets to True to use MQTT over an unsecured websocket on port 80.
# Try this if port 1883 is blocked on your network.
useUnsecuredWebsockets = True

# Set useSSLWebsockets to True to use MQTT over a secure websocket on port 443.
# This type of connection will use slightly more system resources, but the connection
# will be secured by SSL.
useSSLWebsockets = False

###   End of user configuration   ###

# The Hostname of the ThingSpeak MQTT service
mqttHost = "mqtt.thingspeak.com"

# Set up the connection parameters based on the connection type
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global channels
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for channel in channels:
        client.subscribe(channel)
        # The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    global stored_data
    topic = msg.topic
    data = msg.payload
    full_message = topic + "=" + data
    try:
        if stored_data = True:

        publish.single(topic, payload=full_message, hostname=MQTT_HOST, port=tPort, tls=tTLS, transport=tTransport)
        #IF CONNECTED TO INTERNET,
        #PUBLISH TO ThingSpeak
    except:
        #ELSE, SAVE TO CSV TO BE SAVED LATER

# Run a loop which calculates the system performance every
#   20 seconds and published that to a ThingSpeak channel
#   using MQTT.

def save_data():
    filename = "SavedData.xlsx"
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "hello"
    sheet["B1"] = "world!"
    sheet.insert_rows("Date/Time", "field1", "field2", "field3", "field4", "field5")

    workbook.save(filename=filename)


while(True):

    # get the system performance data
    cpuPercent = psutil.cpu_percent(interval=20)
    ramPercent = psutil.virtual_memory().percent
    print (" CPU =",cpuPercent,"   RAM =",ramPercent)

    # build the payload string
    tPayload = "field1=" + str(cpuPercent) + "&field2=" + str(ramPercent)

    # attempt to publish this data to the topic
    try:
        publish.single(topic, payload=tPayload, hostname=MQTT_HOST, port=tPort, tls=tTLS, transport=tTransport)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")
