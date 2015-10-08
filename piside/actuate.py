#!/usr/bin/python

pinList = [12, 16, 18, 22, 32, 38, 37, 35]

setpins=[]

for i in range(1,9):
    try:
        with open('/tmp/desired_relay%d' % (i), 'r') as f:
        val=f.read()
        setpins[i]=val.strip()
    except:
        setpins[i]='off'


for pin in setpins:
    iopin = setpins[pin]
    if iopin == 'off':
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    elif iopin == 'on':
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    else:
        try:
            # Sleep X milliseconds, but no more than 60 seconds
            millisec=(int(iopin) % 6000) / 1000.0
        except:
            pass
