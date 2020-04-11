//This program should run on a computer or raspberry pi as a backup in case no other internet access is available.

//if there is internet access, send the data to the internet as individual data or in CSVs
//if there is no internet access, store the data is a CSV file

//ARDUINO should send mqtt message to a topic of the name field 1, field 2, etc
up to 8.

import paho.mqtt.client as mqtt
