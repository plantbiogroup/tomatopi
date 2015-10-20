#!/bin/bash
## Clever script for making fake temperature and humidity data for
## testing.

# PATH=/home/ec2-user/tomatopi/serverside
PATH=/home/jarl/ws/plantbiogroup/tomatopi/serverside

SEC_PER_HOUR=$((60*60))
SEC_PER_MONTH=$((60*60*24*31))
END=`/usr/bin/date +"%s"`
START=$((END - SEC_PER_MONTH))

/usr/bin/rm ${PATH}/static/measurements

for (( i = $START; i < $END; i += $SEC_PER_HOUR))
do
    TEMP="$((25 + (RANDOM % 2))).$((RANDOM % 10))" # Cleverly hand crafted float.
    HUM="$((80 + (RANDOM % 10))).$((RANDOM % 10))" # Cleverly hand crafted float.
    echo "`/usr/bin/date --date="@$i" +"%FT%T"`,$TEMP,$HUM,1,1,1,1,1,1,1,1" >> ${PATH}/static/measurements
done
serverside/etc/plt.temp.hourly
serverside/etc/plt.humidity.hourly
serverside/etc/plt.temp.daily
serverside/etc/plt.humidity.daily
