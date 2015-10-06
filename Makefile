clean:
	-find . -name \*~ -delete

test: reset
	./test.sh

reset:
	echo -n 25.5 > data/desired_temperature
	echo -n 80.0 > data/desired_humidity
	echo -n > data/measurements
