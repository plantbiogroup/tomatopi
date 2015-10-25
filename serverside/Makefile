CRONS=/etc/cron.hourly/plothourly \
      /etc/cron.daily/plotdaily

clean:
	find . -name \*~ -delete

install: $(CRONS)

uninstall:
	sudo rm $(CRONS)

/etc/cron.hourly/plothourly: etc/plothourly
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@

/etc/cron.daily/plotdaily: etc/plotdaily
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@
