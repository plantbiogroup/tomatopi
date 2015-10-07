#!/usr/bin/python
#
# This file works with the 'phytonaut.py file.  It uploads
# measurements on url encoded form to the server and gets the desired
# conrol values back.

import pycurl
import urllib
import StringIO
import os

outbuf = StringIO.StringIO()

field = {}

## Get the data collected so far
try:
    with open('/tmp/measurements', 'r') as f:
        buf = f.read()
        field['data']= buf
except:
    pass

## Get the ifconfig for ease of use
try:
    ifconfig=os.popen('/sbin/ifconfig').read()
    field['ifconfig'] = ifconfig
except:
    pass

c = pycurl.Curl()
c.setopt(c.URL, 'http://phytonaut/measurements')
c.setopt(c.POSTFIELDS, urllib.urlencode(field))
c.setopt(pycurl.WRITEFUNCTION, outbuf.write)
c.perform()

## Now get the result from the call.  It should be two floats, Temp
## and Humidity
desired_temperature_file='/tmp/desired_temperature'
desired_humidity_file='/tmp/desired_humudity'
desired_relay1_file='/tmp/desired_relay1'
desired_relay2_file='/tmp/desired_relay2'
desired_relay3_file='/tmp/desired_relay3'
desired_relay4_file='/tmp/desired_relay4'
desired_relay5_file='/tmp/desired_relay5'
desired_relay6_file='/tmp/desired_relay6'
desired_relay7_file='/tmp/desired_relay7'
desired_relay8_file='/tmp/desired_relay8'

line = outbuf.getvalue()
string = line.split()
desired_temperature=float(string[0])
desired_humidity=float(string[1])
desired_relay1=int(string[2])
desired_relay2=int(string[3])
desired_relay3=int(string[4])
desired_relay4=int(string[5])
desired_relay5=int(string[6])
desired_relay6=int(string[7])
desired_relay7=int(string[8])
desired_relay8=int(string[9])

with open(desired_temperature_file, 'w') as f:
    f.write( '%0.1f' % (desired_temperature))

with open(desired_humidity_file, 'w') as f:
    f.write( '%0.1f' % (desired_humidity))

with open('/tmp/measurements', 'w') as f:
    f.write( '' )

with open(desired_relay1_file, 'w') as f:
    f.write( '%d' % (desired_relay1))

with open(desired_relay2_file, 'w') as f:
    f.write( '%d' % (desired_relay2))

with open(desired_relay3_file, 'w') as f:
    f.write( '%d' % (desired_relay3))

with open(desired_relay4_file, 'w') as f:
    f.write( '%d' % (desired_relay4))

with open(desired_relay5_file, 'w') as f:
    f.write( '%d' % (desired_relay5))

with open(desired_relay6_file, 'w') as f:
    f.write( '%d' % (desired_relay6))

with open(desired_relay7_file, 'w') as f:
    f.write( '%d' % (desired_relay7))

with open(desired_relay8_file, 'w') as f:
    f.write( '%d' % (desired_relay8))

