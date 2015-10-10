BIN=/usr/local/bin/

BINS=${BIN}analyze.py \
	${BIN}actuate.py \
	${BIN}temp.py \
	${BIN}tempuploader.py \
	${BIN}cam.sh \
	${BIN}camuploader.sh

${BIN}analyze.py: analyze.py
	sudo cp $^ $@

${BIN}actuate.py: actuate.py
	sudo cp $^ $@

${BIN}temp.py: temp.py
	sudo cp $^ $@

${BIN}tempuploader.py: tempuploader.py
	sudo cp $^ $@

${BIN}cam.sh: cam.sh
	sudo cp $^ $@

${BIN}camuploader.sh: camuploader.sh
	sudo cp $^ $@

crontab:
	sudo crontab -u root cron.tab

install: ${BINS} crontab

clean:
	find . -name \*~ -delete
