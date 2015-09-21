#!/bin/python

import Adafruit_DHT

##  Possible sensors
##  Adafruit_DHT.DHT11
##  Adafruit_DHT.DHT22
##  Adafruit_DHT.AM2302
sensor = Adafruit_DHT.AM2302

##  The pin is the GPIO pin number not the
##  number of the pin on the 40-pin head
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if temperature is not None:
    with open('/tmp/temperature', 'w') as tmp:
        tmp.write('%0.1f' % (temperature))
if humidity is not None:
    with open('/tmp/humidity', 'w') as tmp:
        tmp.write('%0.1f' % (humidity))
