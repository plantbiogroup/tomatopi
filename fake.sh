#!/bin/bash
## Clever script for making fake temperature and humidity data for
## testing.

SEC_PER_HOUR=$((60*60))
SEC_PER_MONTH=$((60*60*24*31))
END=`date +"%s"`
START=$((END - SEC_PER_MONTH))

echo "--$START--$SEC_PER_MONTH--$END--"

for (( i = $START; i < $END; i += $SEC_PER_HOUR))
do
    TEMP="$((25 + (RANDOM % 2))).$((RANDOM % 10))" # Cleverly hand crafted float.
    HUM="$((80 + (RANDOM % 10))).$((RANDOM % 10))" # Cleverly hand crafted float.
    echo "`date --date="@$i" +"%FT%T"`,$TEMP,$HUM,1,1,1,1,1,1,1,1"
done
