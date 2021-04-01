from flask import Flask,render_template
import pandas as pd
import pygal
import os
import subprocess

app = Flask(__name__)
datapath = '/data'

@app.route('/box/')
def show_box_plot():
    data_array = os.listdir(datapath)
    data_array.sort()
    recent_data = data_array[-1]
    df = pd.read_csv(datapath + '/' + recent_data)

    # date information
    numeric_string = recent_data[10:]
    date_year = numeric_string.split('-')[0] 
    date_month = numeric_string.split('-')[1]
    date_day = numeric_string.split('-')[2]
    date_string = date_month + '-' + date_day + '-' + date_year

    box_plot = pygal.Box()
    box_plot.title = 'Average Sensor readings ' + date_string
    box_plot.add('Temperature', df['temperature'].tolist())
    box_plot.add('Humidity', df['humidity'].tolist())
    return box_plot.render_response()


#@app.route('/')
#def index():
#    sensorData = {
#        "Temperature": currentTemperature,
#        "Humidity": currentHumidity
#    }
#    return render_template("index.html",**sensorData)
#
if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
