#!/usr/bin/python

import time
import sys

rel=[1.0]*10
temperature=None
humidity=None

desired_measurements='/tmp/measurements'
desired_relay_file='/tmp/desired_relay'

## Make an actual temp and humidity read
def read_temp():
    global temperature
    global humidity
    ##  Possible sensors
    ##  Adafruit_DHT.DHT11
    ##  Adafruit_DHT.DHT22
    ##  Adafruit_DHT.AM2302
    sensor = Adafruit_DHT.AM2302

    ##  The pin is the GPIO pin number not the
    ##  number of the pin on the 40-pin head
    pin = 16

    ## The /tmp/temperature is the file we use to register the latest
    ## temperature measurement.  The file /tmp/humidity is the file we use
    ## to register the latest humidity measurement

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if temperature is not None:
        with open('/tmp/temperature', 'w') as tmp:
            tmp.write('%0.1f' % (temperature))
    if humidity is not None:
        with open('/tmp/humidity', 'w') as tmp:
            tmp.write('%0.1f' % (humidity))

## Make up random crap for test purposes
def makeup_temp():
    global temperature
    global humidity

    temperature=25.0 + (random.randint(0,50) / 10.0)
    humidity=50.0 + (random.randint(0,50) / 10.0)

## Write the result of the reads
def writeout():
    ## Append the measurements to the /tmp/measurements file.
    ## This stores the latest series of temperature measurements we have.
    ## The format is:
    ## YYYY-MM-DDThh:mm:ss temperature humidity

    for i in range(1,9):
        try:
            with open('%s%d' % (desired_relay_file,i), 'r') as f:
                rel[i]=f.read().strip()
        except:
            pass

    if temperature is not None and humidity is not None:
        with open(desired_measurements, 'a') as tmp:
            tmp.write('%s,%0.1f,%0.1f,%d,%d,%d,%d,%d,%d,%d,%d\n' %
                      (time.strftime("%FT%T"),
                       temperature,
                       humidity,
                       rel[1],
                       rel[2],
                       rel[3],
                       rel[4],
                       rel[5],
                       rel[6],
                       rel[7],
                       rel[8]))


if __name__ == '__main__':
    # If the first arg is 'test' we fake the data
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        import random
        makeup_temp()               # Just make something up for testing.
    else:
        import Adafruit_DHT
        read_temp()                 # Read the real temp
    writeout()
