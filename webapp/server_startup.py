import pygal
import os
import pandas as pd

datapath = '/data'

def get_daily_average(filename):
    df = pd.read_csv(datapath + '/' + filename)
    file_date = create_date_string(filename)
    temps = df['temperature'].tolist()
    humids = df['humidity'].tolist()
    return sum(temps)/len(temps), sum(humids)/len(humids)

def create_svg(name_list, temp_list, humid_list):
    temp_line = pygal.Line(x_label_rotation=30)
    temp_line.title = 'Temperature °C last 10 days'
    temp_line.x_labels = name_list
    temp_line.add('Average', temp_list)
    temp_line.render_to_file ('static/temperature.svg')

    humid_line = pygal.Line(x_label_rotation=30)
    humid_line.title = 'Humidity percent last 10 days'
    humid_line.x_labels = name_list
    humid_line.add('Average', humid_list)
    humid_line.render_to_file('static/humidity.svg')

def create_date_string(filename):
    numeric_string = filename[10:]
    date_year = numeric_string.split('-')[0] 
    date_month = numeric_string.split('-')[1]
    date_day = numeric_string.split('-')[2]
    return date_month + '-' + date_day + '-' + date_year

def create_svg_start():
    files = os.listdir(datapath)
    files.sort()
    files = files[-10:] # get last ten days of data
    avg_temps = []
    avg_humidities = []
    dates_list = []

    for filename in files:
        avg_temp, avg_humidity = get_daily_average(filename)
        avg_temps.append(round(avg_temp, 3))
        avg_humidities.append(round(avg_humidity, 3))
        dates_list.append(create_date_string(filename))
    
    create_svg(dates_list, avg_temps, avg_humidities)
    
if __name__ == "__main__":
    create_svg_main()