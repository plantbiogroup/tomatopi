#!/bin/bash

## See AM2302.py for explanation of /tmp/measurements
## Upload all the measurements we have collected, and remove the /tmp/measurements file
curl -X POST --data-urlencode data@/tmp/measurements http://example.com/measurements > /dev/null 2>&1 rm /tmp/measurements

## Pictures???
curl ----
