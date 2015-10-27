CRONS=/etc/cron.d/plothourlypart \
      /etc/cron.d/plotdailypart \
      /usr/local/bin/plothourly \
      /usr/local/bin/plotdaily

clean:
	find . -name \*~ -delete

install: $(CRONS)

uninstall:
	sudo rm $(CRONS)

/etc/cron.d/plothourlypart: etc/plothourlypart
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@

/etc/cron.d/plotdailypart: etc/plotdailypart
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@

/usr/local/bin/plotdaily: etc/plotdaily
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@

/usr/local/bin/plothourly: etc/plothourly
	sudo cp $^ $@
	sudo chmod 755 $@
	sudo chown root.root $@
