from flask import Flask
from flask import request


app = Flask(__name__)

defaulttemp = 20
desired_temperature = defaulttemp
desired_temperature_file="desired_temperature"

defaulthumidity = 80
desired_humidity=defaulthumidity
desired_humidity_file="desired_humidity"

measurements_file = "measurements"

@app.route('/measurements', methods=['POST'])
def tomato():
    data = request.form.get('data')
    with open(measurements_file, 'a') as f:
        f.write(data)
    # Return desired TEMP and HUMIDITY
    return "%0.1f %0.1f" % (temp, humidity)

## Desired parameters
@app.route('/desired_temp', methods=['POST'])
def settemp():
    global desired_temperature
    try:
        desired_temperature = float(request.form.get('temp'))
        str = "%0.1f" % (desired_temperature)
    except:
        return "Invalid data"
    with open(desired_temperature_file, 'w') as f:
        f.write(str)
    return str

@app.route('/desired_temp', methods=['GET'])
def gettemp():
    return "%0.1f" % (desired_temperature)

@app.route('/desired_humidity', methods=['POST'])
def sethumidity():
    global humidity
    try:
        humidity = float(request.form.get('humidity'))
        str = "%0.1f" % (desired_humidity)
    except:
        return "Invalid data"
    with open(desired_humidity_file, 'w') as f:
        f.write(str)
    return "%0.1f" % (desired_humidity)

@app.route('/desired_humidity', methods=['GET'])
def gethumidity():
    return "%0.1f" % (desired_humidity)

## Actual parameters
@app.route('/actual_temp', methods=['GET'])
def get_actualtemp():
    return "%0.1f" % (desired_temperature)

@app.route('/actual_humidity', methods=['GET'])
def get_actualhumidity():
    return "%0.1f" % (desired_humidity)



if __name__ == '__main__':
    
    try:
        with open(desired_temperature_file, 'r') as f:
            desired_temperature=float(f.read())
    except:
        desired_temperature = defaulttemp

    try:
        with open(desired_humidity_file, 'r') as f:
            desired_humidity=float(f.read())
    except:
        desired_humidity = defaulthumidity

    app.run(debug=True, host='0.0.0.0', port=5000)
