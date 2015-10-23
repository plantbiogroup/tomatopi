CRONS=/etc/cron.hourly/plothourly \
      /etc/cron.daily/plotdaily

clean:
	find . -name \*~ -delete

all: $(CRONS)

/etc/cron.hourly/plothourly: etc/plothourly
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@

/etc/cron.daily/plotdaily: etc/plotdaily
	sudo cp $^ $@
	chmod 755 $@
	chown root.root $@
