# Tomato Pi
Computer controlled tomatoes with laser beams... from Mars.


## Components

* EDiMAX N150 -- WiFi Nano Adapter $9.99 -- Frys
* Samsung USB charger
* Samsung 16 GB Micro flash $7.80  -- Frys
* Raspberry Pi Camera
* AM2302 Temperature and Humidity sensor from Adafruit
* Phenolic protoboard  $ 4.99 -- Frys  Used to make a head for the AM3202
* 8 pin stackable header $1.99 -- Frys  Used to make a head for the AM3202
* Solder and wire.

## Files
* desired_humidity -- store the last good desired humidity setting
* desired_temperature -- store the last good desired temperature setting
* measurements -- cumulative measurements over time. <temperature humidity>

## Packages
We require pycurl and anacron on the Pi.
```
apt-get install python-pycurl
apt-get install anacron
```

## Hardware Considerations

If you have one of those handy little Edimax WiFi USB dongles, you
need to turn off the power management.

Add the following 
```
\#Disable power management
options 8192cu rtw_power_mgnt=0
```
to the file /etc/modprobe.d/8192cu.conf

Also, you might need to turn off the wifi power management in /etc/networks/interfaces.  Add
```
wireless-power off
```
to the wlan{0..4} entry.

Good read on the subject.
```
http://raspberrypi.stackexchange.com/questions/4120/how-to-automatically-reconnect-wifi/5121#5121
http://raspberrypi.stackexchange.com/questions/6957/how-to-disable-raspberry-pi-power-management
```

About relays and relay drivers:
```
http://raspberrypihobbyist.blogspot.com/2012/09/gpio-output-relay-interface.html
https://www.raspberrypi.org/forums/viewtopic.php?t=36225
```

## REST Endpoints

### GET  /desired_temperature
Get the desired temperature in degrees Celcius.
```
curl -X GET http://example.com/desired_temperature
```

### POST /desired_temperature
Set the desired temperature in degrees Celcius.
```
curl -X POST http://example.com/desired_temperature -d temperature=22.5
```

### GET  /desired_humidity
Get the desired humidity in percent.
```
curl -X GET http://example.com/desired_humidity
```

### POST /desired_humidity
Set the desired humidity in percent.
```
curl -X POST http://example.com/desired_humidity -d humidity=82.4
```
 
### GET  /measurements
Get the actual measurements.
```
curl -X GET http://example.com/measurements
```

### POST /picture
Upload a picture.
```
curl -X POST --data-binary foo@/tmp/picture http://example.com/picture
```

### POST /measurements
Upload a seriec of measurements.
```
curl -X POST --data-urlencode foo@/tmp/measurements http://example.com/measurements
```

Each measurement series is newline delimited.  Each value is space delimited.
A series start with ISO date <space> Degree Celcius <space> Humidity in percent

Example:
```
2015-09-23T10:24:17 26.6 38.6
2015-09-23T10:24:17 26.6 38.6
2015-09-23T10:24:52 26.5 38.6
2015-09-23T10:24:58 26.5 38.6
2015-09-23T10:25:01 26.5 38.6
```


### POST /reset
Return system to default state
```
curl -X POST http://example.com/reset
```

### GET /lastmeasurement
Get the time for the last successfull measurement

### GET /actual_humidity
Get the last measured humidity

### GET /actual_temperature
Get the last measured temperature


## CentOS installation
Install Flask
```
yum install python-flask
```

See
https://github.com/skiwithpete/relaypi/blob/master/8port/script5.py

http://hortsci.ashspublications.org/content/43/7/1951.full

http://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

https://learn.adafruit.com/downloads/pdf/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi.pdf
