import RPi.GPIO as GPIO
import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(['tomato.ini', os.path.expanduser('~/tomato.ini'), '/etc/tomato.ini'])

def get_pinlist():
    config = ConfigParser.ConfigParser()
    config.read(['tomato.ini', os.path.expanduser('~/tomato.ini'), '/etc/tomato.ini'])
    return [ int(str) for str in config.get('relays', 'pinList').split(',') ]

def relay_init(pinList):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in pinList:
        GPIO.setup(i, GPIO.OUT)

def get_bool(val):
    if val == 'on':
        return True
    if val == 'off':
        return False;
    return(bool(val))

def set_pin(pin, desired):
    if get_bool(desired):
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def get_relay_state():
    relay_file = config.get('relays', 'relay_file')
    with open(relay_file, 'r') as f:
        return [get_bool(val.strip()) for val in f.readline().split(',') ]
