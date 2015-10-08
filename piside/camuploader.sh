#!/bin/bash

####################################################
##  REMEMBER to add phytonaut to your etc hosts file
####################################################
## file.  Stuff the return value in the file ''response''
/usr/bin/curl -s -X POST --data-binary @/tmp/pict.jpg http://phytonaut/picture && rm /tmp/pict.jpg
