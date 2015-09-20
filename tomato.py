##  This code is based on example code from the good people at Adafruit.

from flask import Flask
import Adafruit_DHT


##  Possible sensors
##  Adafruit_DHT.DHT11
##  Adafruit_DHT.DHT22
##  Adafruit_DHT.AM2302
sensor = Adafruit_DHT.AM2302

##  The pin is the GPIO pin number not the
##  number of the pin on the 40-pin head
pin = 4

app = Flask(__name__)

@app.route('/')
def root():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
	return 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
	return 'Failed to get reading. Try again!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
