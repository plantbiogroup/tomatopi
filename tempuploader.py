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


## Get the data collected so far
try:
    with open('/tmp/measurements', 'r') as f:
        buf = f.read()
except:
    pass

## Get the ifconfig for ease of use
try:
    ifconfig=os.popen('/sbin/ifconfig').read()
except:
    pass

field = {'data': buf,
         'ifconfig': ifconfig}

c = pycurl.Curl()
c.setopt(c.URL, 'http://phytonaut/measurements')
c.setopt(c.POSTFIELDS, urllib.urlencode(field))
c.setopt(pycurl.WRITEFUNCTION, outbuf.write)
c.perform()

## Now get the result from the call.  It should be two floats, Temp
## and Humidity
desired_temperature_file='/tmp/desired_temperature'
desired_humidity_file='/tmp/desired_humudity'

line = outbuf.getvalue()
string = line.split()
desired_temperature=float(string[0])
desired_humidity=float(string[1])

with open(desired_temperature_file, 'w') as f:
    f.write( '%0.1f' % (desired_temperature))

with open(desired_humidity_file, 'w') as f:
    f.write( '%0.1f' % (desired_humidity))

with open('/tmp/measurements', 'w') as f:
    f.write( '' )
