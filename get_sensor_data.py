#!/usr/bin/python3
import os
import datetime
from sense_hat import SenseHat

date = datetime.datetime.now()
path = "/data/"
filename ="sensordata" + str(date.year) + '-' + str(date.month) + '-' + str(date.day)
filepath = path + filename

exists = os.path.exists(filepath)

with open( filepath, "a") as file_object:
    if not exists:
        file_object.write("temperature,humidity,time\n")
    sense = SenseHat()
    temp = round(sense.get_temperature(), 3)
    humidity = round(sense.get_humidity(), 3)    
    file_object.write(str(temp) +',' + str(humidity) + ',' + str(date.hour) +
            ":" + str(date.minute) + '\n')
