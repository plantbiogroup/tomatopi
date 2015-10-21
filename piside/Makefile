BINS=/usr/local/bin/analyze.py \
	/usr/local/bin/actuate.py \
	/usr/local/bin/temp.py \
	/usr/local/bin/cam.sh \
	/usr/local/bin/cycle.sh \
	/etc/cron.d/cam.d \
	/etc/cron.d/cycle.d \
	/etc/cron.hourly/tempuploader.py \
	/etc/cron.hourly/camuploader.sh

/usr/local/bin/cycle.sh: cycle.sh
	sudo cp $^ $@

/usr/local/bin/analyze.py: analyze.py
	sudo cp $^ $@

/usr/local/bin/actuate.py: actuate.py
	sudo cp $^ $@

/usr/local/bin/temp.py: temp.py
	sudo cp $^ $@

/usr/local/bin/cam.sh: cam.sh
	sudo cp $^ $@

/etc/cron.d/cam.d: cam.d
	sudo cp $^ $@

/etc/cron.d/cycle.d: cycle.d
	sudo cp $^ $@

/etc/cron.hourly/tempuploader.py: tempuploader.py
	sudo cp $^ $@

/etc/cron.hourly/camuploader.sh: camuploader.sh
	sudo cp $^ $@

install: ${BINS}

clean:
	find . -name \*~ -delete
