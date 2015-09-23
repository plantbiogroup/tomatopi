#!/bin/bash
H=http://127.0.0.1:80

echo -n "Expecting `cat desired_temperature`:   "
curl -X GET ${H}/desired_temperature
echo

echo -n "Expecting `cat desired_humidity`:   "
curl -X GET ${H}/desired_humidity
echo

TEMP=25.1
echo -n "Expecting $TEMP:   "
curl -X POST ${H}/desired_temperature -d temperature=$TEMP
echo

echo -n "Expecting `cat desired_temperature`:   "
curl -X GET ${H}/desired_temperature
echo

HUM=82.5
echo -n "Expecting $HUM:   "
curl -X POST ${H}/desired_humidity -d humidity=$HUM
echo

echo -n "Expecting `cat desired_humidity`:   "
curl -X GET ${H}/desired_humidity
echo

echo -n "Expecting `cat desired_temperature` `cat desired_humidity`:   "
cat<<EOF>snopp
`date +"FT%T` 10 11
`date +"FT%T` 12 13
`date +"FT%T` 14 15
EOF
curl -X POST --data-urlencode data@snopp ${H}/measurements
echo

echo "Expecting"
cat measurements
echo "Got:"
curl -X GET ${H}/measurements
echo

curl -X POST ${H}/reset
echo -n "Measurements: "
cat measurements
echo
echo -n "Temperature: "
cat desired_temperature
echo
echo -n "Humidity: "
cat desired_humidity
echo

curl -s -X POST --data-binary @${PWD}/test.jpg ${H}/picture
