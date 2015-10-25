BINS=/usr/local/bin/analyze \
	/usr/local/bin/actuate \
	/usr/local/bin/temperature \
	/usr/local/bin/cam \
	/usr/local/bin/cycle \
	/etc/cron.d/campart \
	/etc/cron.d/cyclepart \
	/etc/cron.hourly/tempuploader \
	/etc/cron.hourly/camuploader

/usr/local/bin/cycle: cycle
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/analyze: analyze
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/actuate: actuate
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/temperature: temperature
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/usr/local/bin/cam: cam
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.d/campart: campart
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.d/cyclepart: cyclepart
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.hourly/tempuploader: tempuploader
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.hourly/camuploader: camuploader
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

install: ${BINS}

uninstall:
	sudo rm ${BINS}

clean:
	find . -name \*~ -delete
