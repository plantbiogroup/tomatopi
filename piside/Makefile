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
	chmod 755 $@
	chown root.root $@

/usr/local/bin/analyze.py: analyze.py
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/actuate.py: actuate.py
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/temp.py: temp.py
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/cam.sh: cam.sh
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.d/cam.d: cam.d
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.d/cycle.d: cycle.d
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.hourly/tempuploader.py: tempuploader.py
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.hourly/camuploader.sh: camuploader.sh
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

install: ${BINS}

clean:
	find . -name \*~ -delete
