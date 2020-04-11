#test.py
from __future__ import print_function
import paho.mqtt.publish as publish
import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook


filename = "SavedData.xlsx"
workbook = Workbook()
sheet = workbook.active

sheet.append(["Date/Time", "field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8"])

workbook.save(filename=filename)


import csv
import datetime


data = []

with open('SavedData.csv', mode='w') as csv_file:
    fieldnames = ["datetime","field1","field2","field3","field4"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'datetime': datetime.datetime.now(), "field1": "yo"})
    #writer.writerow(['Erica Meyers', 'IT', 'March'])
