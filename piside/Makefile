BINS=/usr/local/bin/analyze \
	/usr/local/bin/actuate \
	/usr/local/bin/measure \
	/usr/local/bin/cam \
	/usr/local/bin/camuploader \
	/usr/local/bin/cycle \
	/usr/local/bin/publish \
	/usr/local/bin/tomato.ini \
	/etc/cron.d/campart \
	/etc/cron.d/cyclepart \
	/etc/cron.d/publishpart \
	/etc/cron.d/camuploaderpart

/usr/local/bin/cycle: cycle
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/analyze: analyze
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/actuate: actuate
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/measure: measure
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/cam: cam
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/camuploader: camuploader
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/publish: publish
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/usr/local/bin/tomato.ini: tomato.ini
	- sudo cp $^ $@
	- sudo chmod 644 $@
	- sudo chown root.root $@

/etc/cron.d/campart: campart
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/etc/cron.d/cyclepart: cyclepart
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/etc/cron.d/publishpart: publishpart
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

/etc/cron.d/camuploaderpart: camuploaderpart
	- sudo cp $^ $@
	- sudo chmod 755 $@
	- sudo chown root.root $@

install: $(BINS)

uninstall:
	- sudo rm $(BINS)
	- sudo rm /tmp/actual*
	- sudo rm /tmp/desired*
	- sudo rm /tmp/measurements

clean:
	find . -name \*~ -delete
