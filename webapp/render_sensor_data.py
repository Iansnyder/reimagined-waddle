from sense_hat import SenseHat
from time import sleep
from time import asctime
from flask import Flask,render_template

sense = SenseHat()
currentTemperature = round(sense.get_temperature(),3)
currentHumidity = round(sense.get_humidity(),3)
message = "Temperature is %dF. Humidity is %d percent."%(currentTemperature,currentHumidity)

app = Flask(__name__)

@app.route('/')
def index():
    sensorData = {
        "Temperature": currentTemperature,
        "Humidity": currentHumidity
    }
    return render_template("index.html",**sensorData)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
