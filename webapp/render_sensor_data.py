from flask import Flask,render_template,request
import pandas as pd
import pygal
import os
import math
from sense_hat import SenseHat
from time import sleep
from time import asctime
from server_startup import create_svg_start, create_date_string

sense = SenseHat()
currentTemperature = round(sense.get_temperature(),3)
currentHumidity = round(sense.get_humidity(),3)
message = "Temperature is %dF. Humidity is %d percent."%(currentTemperature,currentHumidity)

create_svg_start()

app = Flask(__name__)
datapath = '/data'

@app.route('/selectbox', methods = ['GET','POST'])
def show_box_plot_single():
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

@app.route('/box/')
def show_box_plot():
    data_array = os.listdir(datapath)
    data_array.sort()
    today_file = data_array[-1]
    yesterday_file = data_array[-2]
    df_today = pd.read_csv(datapath + '/' + today_file)
    df_yesterday = pd.read_csv(datapath + '/' + yesterday_file)
    # date information
    today_date_string = create_date_string(today_file)
    yesterday_date_string = create_date_string(yesterday_file)


    box_plot = pygal.Box()        # range does not seem to work
    box_plot.zero = min(df_today['temperature']) - .2
    box_plot.title = 'Average Temperature readings Celcius'
    box_plot.add(today_date_string, df_today['temperature'].tolist())
    box_plot.add(yesterday_date_string, df_yesterday['temperature'].tolist())
    return box_plot.render_response()
    

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
