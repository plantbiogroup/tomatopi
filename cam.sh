#!/bin/bash

## -t -- Timeout for taking a picture
## -w -- width set to 256 for small data size
## -h -- height set to 256 for small data size
## -q -- quality <0 - 100>  set to 50 for small data size
## -n -- no preview, easier on the processor.
## Cheap and easy setting
raspistill -t 0 -n -w 256 -h 256 -q 50 -o /tmp/tomatopi.jpg

## Uncomment for high quality settings
## Comment out the all the other ''raspistill'' lines
# raspistill -t 0 -n -w 1024 -h 1024 -q 100 -o /tmp/tomatopi.jpg
