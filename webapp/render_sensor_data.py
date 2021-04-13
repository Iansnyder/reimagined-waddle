from flask import Flask,render_template,request
import pandas as pd
import pygal
import os
import math
from sense_hat import SenseHat
from time import sleep
from time import asctime

sense = SenseHat()
currentTemperature = round(sense.get_temperature(),3)
currentHumidity = round(sense.get_humidity(),3)
message = "Temperature is %dF. Humidity is %d percent."%(currentTemperature,currentHumidity)

app = Flask(__name__)
datapath = '/data'

@app.route('/selectbox', methods = ['GET','POST'])
def show_box_plot():
    select = request.form.get('dropdownitem')
    today_file = select
    df_today = pd.read_csv(datapath + '/' + today_file)

    #date information
    today_date_string = create_date_string(today_file)

    box_plot = pygal.Box()
    box_plot.zero = min(df_today['temperature']) - .2
    box_plot.title = 'Average Temperature readings Celcius'
    box_plot.add(today_date_string, df_today['temperature'])
    
    return box_plot.render_response()

def create_date_string(filename):
    numeric_string = filename[10:]
    date_year = numeric_string.split('-')[0] 
    date_month = numeric_string.split('-')[1]
    date_day = numeric_string.split('-')[2]
    return date_month + '-' + date_day + '-' + date_year

@app.route('/')
def index():
    data_array = os.listdir(datapath)
    data_array.sort()

    sensorData = {
        "Temperature": currentTemperature,
        "Humidity": currentHumidity,
        "dropdown": data_array
    }
    return render_template("index.html",**sensorData)

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
