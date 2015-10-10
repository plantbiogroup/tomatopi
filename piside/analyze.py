#!/usr/bin/python
## Analyze what needs to be done.
import datetime

now = datetime.datetime.now()
## Relay 1, light
try:
    with open(desired_light_on_file, 'r') as f:
        desired_light_on = f.read()
        on_h, on_min, on_sec = desired_light_on.split(':')
        light_on = desired_light_on.replace(hour=on_h, minute=on_min, second=on_sec)
except:
    pass

try:
    with open(desired_light_off_file, 'r') as f:
        desired_light_off = f.read()
        off_h, off_min, off_sec = desired_light_off.split(':')
        light_off = desired_light_off.replace(hour=off_h, minute=off_min, secoffd=off_sec)
except:
    pass

if light_on < now and now < light_off:
    print "/tmp/desired_relay1 on"
else:
    print "/tmp/desired_relay1 off"

## Relay 2 Heat

## Relay 3 Humidity

## Relay 4 CO2
