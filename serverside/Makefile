CRONS=/etc/cron.daily/plt.humidity.daily \
      /etc/cron.daily/plt.temperature.daily
clean:
	find . -name \*~ -delete

all: $(CRONS)
	mkdir -p daily/humidity
	mkdir -p daily/temp

/etc/cron.hourly/plt.humidity.hourly: etc/plt.humidity.hourly
	sudo cp $^ $@

/etc/cron.hourly/plt.temp.hourly: etc/plt.temp.hourly
	sudo cp $^ $@

/etc/cron.daily/plt.temp.daily: etc/plt.temp.daily
	sudo cp $^ $@

