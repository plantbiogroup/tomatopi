#!/usr/bin/python                                                                                                   
import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

# init list with pin numbers                                                                                        

#pinList = [2, 3, 4, 17, 27, 22, 10, 9]
pinList = [12, 16, 18, 22, 32, 38, 37, 35]

# loop through pins and set mode and state to 'low'                                                                 

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop                                                                 

SleepTimeS = 0.2
SleepTimeL = 0.5

# main loop                                                                                                         

try:
      for i in pinList:
         GPIO.output(i, GPIO.LOW)


# End program cleanly with keyboard                                                                                 
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings                                                                                             
  # GPIO.cleanup()

