# Tomato Pi
Computer controlled tomatoes with laser beams... from Mars.


## Components

* EDiMAX N150 -- WiFi Nano Adapter $9.99 -- Frys
* Samsung USB charger
* Samsung 16 GB Micro flash $7.80  -- Frys
* Raspberry Pi Camera
* AM2302 Temperature and Humidity sensor from Adafruit
* Phenolic protoboard  $ 4.99 -- Frys  Used to make a head for the AM3202
* 8 pin stackable header $1.99 -- Frys  Used to make a head for the AM3202
* Solder and wire.

## Files
* desired_humidity -- store the last good desired humidity setting
* desired_temperature -- store the last good desired temperature setting
* measurements -- cumulative measurements over time. <temperature humidity>

## REST Endpoints

### GET  /desired_temperature
Get the desired temperature in degrees Celcius.
```
curl -X GET http://example.com/desired_temperature
```

### POST /desired_temperature
Set the desired temperature in degrees Celcius.
```
curl -X POST http://example.com/desired_temperature -d temperature=22.5
```

### GET  /desired_humidity
Get the desired humidity in percent.
```
curl -X GET http://example.com/desired_humidity
```

### POST /desired_humidity
Set the desired humidity in percent.
```
curl -X POST http://example.com/desired_humidity -d humidity=82.4
```
 
### GET  /measurements
Get the actual measurements
```
curl -X GET http://example.com/measurements
```

### POST /reset
Return system to default state
```
curl -X POST http://example.com/reset
```
