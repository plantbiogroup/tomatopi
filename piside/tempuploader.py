#!/usr/bin/python
#
# This file works with the 'phytonaut.py file.  It uploads
# measurements on url encoded form to the server and gets the desired
# conrol values back.

import StringIO
import json
import os
import pycurl
import sys
import urllib

outbuf = StringIO.StringIO()

field = {}

def report_measurements(endpoint):
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
    c.setopt(c.URL, endpoint)
    c.setopt(c.POSTFIELDS, urllib.urlencode(field))
    c.setopt(pycurl.WRITEFUNCTION, outbuf.write)
    c.perform()
    
    ## Now get the result from the call.  It should be two floats, Temp
    ## and Humidity
    desired_temperature_file='/tmp/desired_temperature'
    desired_humidity_file='/tmp/desired_humudity'
    desired_relay_file='/tmp/desired_relay'
    
    line = outbuf.getvalue()
    vals = json.loads(line)
    desired_temperature=vals['desired_temperature']
    desired_humidity=vals['desired_humidity']
    desired_light_on=vals['desired_light_on']
    desired_light_off=vals['desired_light_off']

    with open(desired_temperature_file, 'w') as f:
        f.write( '%0.1f' % (desired_temperature))
    
    with open(desired_humidity_file, 'w') as f:
        f.write( '%0.1f' % (desired_humidity))
    
    with open('/tmp/measurements', 'w') as f:
        f.write( '' )               # Clear measurements
    
    
    for i in range(1,9):
        with open('desired_relay_file%d' % (i), 'w') as f:
            f.write(vals['relays'][i])
    
if __name__ == '__main__':
    # If the first arg is 'test' we fake the data
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        report_measurements('http://127.0.0.1/measurements')
    else:
        report_measurements('http://phytonaut/measurements')
