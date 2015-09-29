#!/bin/bash

####################################################
##  REMEMBER to add phytonaut to your etc hosts file
####################################################
## See AM2302.py for explanation of /tmp/measurements Upload all the
## measurements we have collected, and remove the /tmp/measurements
## file.  Stuff the return value in the file ''response''
/usr/bin/curl -s -X POST --data-urlencode ifconfig@/tmp/ifconfig http://phytonaut/ifconfig > /tmp/response && rm /tmp/ifconfig
