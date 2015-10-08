#!/bin/python

from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import flash
import os.path
import os

app = Flask(__name__)

defaulttemperature = 20
desired_temperature = defaulttemperature
desired_temperature_file="desired_temperature"

defaulthumidity = 80
desired_humidity=defaulthumidity
desired_humidity_file="desired_humidity"

measurements_file = "measurements"
ifconfig_file = "static/ifconfig"

lastmeasurement=None
actual_temperature=None
actual_humidity=None

picture_file="static/picture.jpg"
ifconfig_data=None

relay=[None]*8
val=[None]*10

####################
## Reset to default
@app.route('/reset', methods=['POST'])
def reset_to_default():
    str = 'ok'
    try:
        with open(measurements_file, 'w') as f:
            f.write('')
    except:
        str='Measurements not reset.'
    try:
        desired_humidity=defaulthumidity
        with open(desired_humidity_file, 'w') as f:
            f.write('%0.1f' % (defaulthumidity))
    except:
        str+=' Humidity not reset'
    try:
        desired_temperature=defaulttemperature
        with open(desired_temperature_file, 'w') as f:
            f.write('%0.1f' % (defaulttemperature))
    except:
        str+=' Temperature not reset'
    return str

####################
## Set measurements
@app.route('/measurements', methods=['POST'])
def set_measurements():
    global lastmeasurement
    global actual_temperature
    global actual_humidity
    global ifconfig_data
    global relay
    global val

    # Process the data
    try:
        data = request.form.get('data')
        print "Data -> %s" % (data)
        # Dump data into the measurements file
        with open(measurements_file, 'a') as f:
            f.write(data)
        # Get the latest values
        t = data.splitlines()
        q = t[len(t) - 1]
        lastmeasurement, actual_temperature, actual_humidity, relay[1], relay[2], relay[3], relay[4], relay[5], relay[6], relay[7], relay[8] = q.split(',')
    except:
        print "measurement -> %s" % (data)

    try:
        ifconfig_data = request.form.get('ifconfig')
        print "IfConfig -> %s" % (ifconfig_data)
        with open(ifconfig_file, 'w') as f:
            f.write(ifconfig_data)
    except:
        pass

    for i in range(1,9):
        print "val %d" %(i)
        try:
            with open('data/desired_relay%d' % (i), 'r') as f:
                val[i]=f.read().strip()
        except:
            val[i]='off'

    # Return desired TEMP and HUMIDITY
    return "%0.1f %0.1f %s %s %s %s %s %s %s %s" % (desired_temperature,
                                                    desired_humidity,
                                                    val[1],
                                                    val[2],
                                                    val[3],
                                                    val[4],
                                                    val[5],
                                                    val[6],
                                                    val[7],
                                                    val[8]
    )

@app.route('/picture', methods=['POST'])
def set_picture():

    # Process the picture
    data = request.stream.read()
    with open(picture_file, 'w') as f:
        f.write(data)
    return 'ok'

@app.route('/measurements', methods=['GET'])
def get_measurements():
    with open(measurements_file, 'r') as f:
        str=f.read()
    return "%s" % (str)

####################
## Get DESIRED values
@app.route('/desired_temperature', methods=['GET'])
def get_desired_temp():
    with open(desired_temperature_file, 'r') as f:
        str = f.read()
    return str

@app.route('/desired_humidity', methods=['GET'])
def get_desired_humidity():
    with open(desired_humidity_file, 'r') as f:
        str = f.read()
    return str


####################
## Set DESIRED values
@app.route('/desired_humidity', methods=['POST'])
def set_humidity():
    global desired_humidity
    try:
        desired_humidity = float(request.form.get('humidity'))
        str = "%0.1f" % (desired_humidity)
    except:
        return "Invalid data"
    with open(desired_humidity_file, 'w') as f:
        f.write(str)
    return "%0.1f" % (desired_humidity)

@app.route('/desired_temperature', methods=['POST'])
def set_temperature():
    global desired_temperature
    try:
        desired_temperature = float(request.form.get('temperature'))
        str = "%0.1f" % (desired_temperature)
    except:
        return "Invalid data"
    with open(desired_temperature_file, 'w') as f:
        f.write(str)
    return "%0.1f" % (desired_temperature)


####################
## Get ACTUAL values
@app.route('/actual_temp', methods=['GET'])
def get_actual_temperature():
    try:
        return "%0.1f" % (actual_temperature)
    except:
        return 'fail'

@app.route('/actual_humidity', methods=['GET'])
def get_actual_humidity():
    try:
        return "%0.1f" % (actual_humidity)
    except:
        return 'fail'

@app.route('/lastmeasurement', methods=['GET'])
def get_lastmeasurement():
    try:
        if lastmeasurement is not None:
            return "%s" % (lastmeasurement)
    except:
        pass
    return 'fail'

####################
## Main
@app.route('/', methods=['GET'])
def index():
    if os.path.isfile("static/picture.jpg") and os.stat("static/picture.jpg").st_size != 0:
        file = "/static/picture.jpg"
    else:
        file = "/static/default.png"
    return render_template('index.html',
                           defaulttemperature=defaulttemperature,
                           desired_temperature=desired_temperature,
                           defaulthumidity=defaulthumidity,
                           desired_humidity=desired_humidity,
                           actual_temperature=actual_temperature,
                           actual_humidity=actual_humidity,
                           ifconfig_data=ifconfig_data,
                           file=file,
                           relay=relay)


####################
## Main
if __name__ == '__main__':
    try:
        with open(desired_temperature_file, 'r') as f:
            desired_temperature=float(f.read())
    except:
        desired_temperature = defaulttemperature

    try:
        with open(desired_humidity_file, 'r') as f:
            desired_humidity=float(f.read())
    except:
        desired_humidity = defaulthumidity

    app.run(debug=True, host='0.0.0.0', port=80)
