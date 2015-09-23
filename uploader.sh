#!/bin/bash

## See AM2302.py for explanation of /tmp/measurements Upload all the
## measurements we have collected, and remove the /tmp/measurements
## file.  Stuff the return value in the file ''response''
curl -s -X POST --data-urlencode data@/tmp/measurements http://example.com/measurements > response && rm /tmp/measurements

## Pictures???
## curl ----
