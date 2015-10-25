#!/bin/python

from flask import Flask
from flask import flash
from flask import g
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from os import listdir
from os.path import isfile, join
import datetime
import os
import os.path
import shutil

app = Flask(__name__)

tdelta = datetime.timedelta(minutes=15)
a_day = datetime.timedelta(hours=24)
midnight = datetime.timedelta()

defaultlight_on = datetime.timedelta(hours=6)
desired_light_on = defaultlight_on
desired_light_on_file="desired_light_on"

defaultlight_off = datetime.timedelta(hours=22)
desired_light_off = defaultlight_off
desired_light_off_file="desired_light_off"

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
upload_picture_file="static/upload.jpg"
ifconfig_data=None


def new_time(nt):
    if nt >= a_day:
        return midnight
    elif nt < midnight:
        return a_day - tdelta
    else:
        return nt

def desired_relay(relay):
    try:
        with open('data/desired_relay%d' % (relay), 'r') as f:
            val = f.read().strip()
            if(val == '1'):
                val = 'on'
    except:
        val ='off'


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
    try:
        desired_light_on=defaultlight_on
        with open(desired_light_on_file, 'w') as f:
            f.write('%s' % (str(defaultlight_on)))
    except:
        str+=' Light_on not reset'
    try:
        desired_light_off=defaultlight_off
        with open(desired_light_off_file, 'w') as f:
            f.write('%s' % (str(defaultlight_off)))
    except:
        str+=' Light_off not reset'
    return str

####################
## Set measurements
@app.route('/measurements', methods=['POST'])
def set_measurements():
    global lastmeasurement
    global actual_temperature
    global actual_humidity
    global ifconfig_data

    relay = []


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
        lastmeasurement, actual_temperature, actual_humidity, relay[1], relay[2], relay[3], relay[4] = q.split(',')
    except:
        print "measurement -> %s" % (data)

    try:
        ifconfig_data = request.form.get('ifconfig')
        print "IfConfig -> %s" % (ifconfig_data)
        with open(ifconfig_file, 'w') as f:
            f.write(ifconfig_data)
    except:
        pass

    parameters = {'desired_temperature' : desired_temperature,
                  'desired_humidity' : desired_humidity,
                  'desired_light_on' : str(desired_light_on),
                  'desired_light_off': str(desired_light_off)
    }
    for i in range(1,5):
        parameters["desired_relay%d" % (i)] = desired_relay(i)

    return jsonify( parameters )

@app.route('/picture', methods=['POST'])
def set_picture():

    # Process the picture
    data = request.stream.read()
    with open(upload_picture_file, 'w') as f:
        f.write(data)
    shutil.copy(upload_picture_file, picture_file)
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
        if request.form.get('humidity') == 'inc':
            desired_humidity += 1.0
        elif request.form.get('humidity') == 'dec':
            desired_humidity -= 1.0
        else:
            desired_humidity = float(request.form.get('humidity'))
    except:
        pass
    return redirect(url_for('biodome'))

@app.route('/desired_temperature', methods=['POST'])
def set_temperature():
    global desired_temperature
    try:
        if request.form.get('temperature') == 'inc':
            desired_temperature += 1.0
        elif request.form.get('temperature') == 'dec':
            desired_temperature -= 1.0
        else:
            desired_temperature = float(request.form.get('temperature'))
    except:
        pass
    return redirect(url_for('biodome'))

@app.route('/desired_light_on', methods=['POST'])
def set_light_on():
    global desired_light_on
    try:
        if request.form.get('light_on') == 'inc':
            desired_light_on = new_time(desired_light_on + tdelta)
        elif request.form.get('light_on') == 'dec':
            desired_light_on = new_time(desired_light_on - tdelta)
        else:
            pass
    except:
        pass
    return redirect(url_for('biodome'))

@app.route('/desired_light_off', methods=['POST'])
def set_light_off():
    global desired_light_off
    try:
        if request.form.get('light_off') == 'inc':
            desired_light_off = new_time(desired_light_off + tdelta)
        elif request.form.get('light_off') == 'dec':
            desired_light_off = new_time(desired_light_off - tdelta)
        else:
            pass
    except:
        pass
    return redirect(url_for('biodome'))

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
## biodome
@app.route('/biodome', methods=['GET'])
def biodome():
    if os.path.isfile("static/picture.jpg") and os.stat("static/picture.jpg").st_size != 0:
        file = "/static/picture.jpg"
    else:
        file = "/static/default.png"

    dailytempdir = 'static/daily/temp/'
    dailytemps = [ f for f in listdir(dailytempdir) if isfile(join(dailytempdir,f)) ]

    dailyhumiditiedir = 'static/daily/humidity/'
    dailyhumidities = [ f for f in listdir(dailyhumiditiedir) if isfile(join(dailyhumiditiedir,f)) ]

    weeklytempdir = 'static/weekly/temp/'
    weeklytemps = [ f for f in listdir(weeklytempdir) if isfile(join(weeklytempdir,f)) ]

    weeklyhumiditiedir = 'static/weekly/humidity/'
    weeklyhumidities = [ f for f in listdir(weeklyhumiditiedir) if isfile(join(weeklyhumiditiedir,f)) ]

    return render_template('biodome.html',
                           defaultlight_on=defaultlight_on,
                           defaultlight_off=defaultlight_off,
                           desired_light_on=desired_light_on,
                           desired_light_off=desired_light_off,
                           defaulttemperature=defaulttemperature,
                           desired_temperature=desired_temperature,
                           defaulthumidity=defaulthumidity,
                           desired_humidity=desired_humidity,
                           actual_temperature=actual_temperature,
                           actual_humidity=actual_humidity,
                           ifconfig_data=ifconfig_data,
                           file=file,
                           dailytemps=dailytemps,
                           dailyhumidities=dailyhumidities,
                           weeklytemps=weeklytemps,
                           weeklyhumidities=weeklyhumidities,
                           relay=relay)


####################
## Root
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

####################
## Main
if __name__ == '__main__':
    try:
        with open(desired_light_on_file, 'r') as f:
            desired_light_on=float(f.read())
    except:
        desired_light_on = defaultlight_on

    try:
        with open(desired_light_off_file, 'r') as f:
            desired_light_off=float(f.read())
    except:
        desired_light_off = defaultlight_off

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
