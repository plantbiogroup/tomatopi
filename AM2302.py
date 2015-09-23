#!/usr/bin/python

import time
import Adafruit_DHT

##  Possible sensors
##  Adafruit_DHT.DHT11
##  Adafruit_DHT.DHT22
##  Adafruit_DHT.AM2302
sensor = Adafruit_DHT.AM2302

##  The pin is the GPIO pin number not the
##  number of the pin on the 40-pin head
pin = 4

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

## Append the measurements to the /tmp/measurements file.
## This stores the latest series of temperature measurements we have.
## The format is:
## YYYY-MM-DDThh:mm:ss temperature humidity
if temperature is not None and humidity is not None:
    with open('/tmp/measurements', 'a') as tmp:
        tmp.write('%s %0.1f %0.1f\n' % (time.strftime("%FT%T"), temperature, humidity))
