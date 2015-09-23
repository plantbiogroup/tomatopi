clean:
	-find . -name \*~ -delete

test: reset
	./test.sh

reset:
	echo -n 25.5 > desired_temperature
	echo -n 80.0 > desired_humidity
	echo -n > measurements
