## Code inspired by
## http://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Run as root.")

def flippit():
    ## Set board pin numbering
    GPIO.setmode(GPIO.BOARD)

    ## Find out the state of the pin
    GPIO.setup(channel, GPIO.IN)
    ## READ the channel
    ## returns 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True
    pinval = GPIO.input(channel)

    if pinval == 0 or pinval == GPIO.LOW or pinval == False:
        newpinval = GPIO.HIGH
    else:
        newpinval = GPIO.LOW
        
    ## Now set the channel
    GPIO.setup(channel, GPIO.OUT)

    ## Cleanup
    GPIO.cleanup(channel)
    return

if __name-- == '__main__':
    channel = int(argv[1])
    flippit()
