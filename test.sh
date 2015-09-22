#!/bin/bash
H=http://127.0.0.1:5000

curl -X GET ${H}/desired_temp
echo
curl -X GET ${H}/desired_humidity
echo

curl -X POST ${H}/desired_temp -d temp=25.1
echo
curl -X GET ${H}/desired_temp
echo

curl -X POST ${H}/desired_humidity -d humidity=82.5
echo
curl -X GET ${H}/desired_humidity
echo



# curl -X POST --data data@/tmp/measurements ${H}/measurements
