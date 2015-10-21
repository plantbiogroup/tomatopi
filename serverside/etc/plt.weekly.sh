#!/bin/bash
## Every day, plot a weeks worth of data

# P=/home/ec2-user/tomatopi/serverside
P=/home/jarl/ws/plantbiogroup/tomatopi/serverside

NAME=`date +%Ywk%V`

plot_graph()
{
    mkdir -p ${P}/static/${1}/${2}
    find ${P}/static/${1}/${2} -type f -mtime +32 -delete
    cat<<-EOF | gnuplot
	set xdata time
	set timefmt "${TIMEFMT}"
	set format x "%a %d %b"
	set datafile separator ","
	set grid
	set ylabel "${3}"
	set xlabel "Day of week"
	set terminal png size 1200,300 enhanced font "Helvetica,8"
	set output "${P}/static/${1}/${2}/${NAME}.png"
	plot ["${THEN}":"${NOW}"] "${P}/static/measurements" using 1:${5} with lines title "${4}"
EOF
}

TIMEFMT="%Y-%m-%dT%H:%M:%S"
NOW=`/bin/date +"${TIMEFMT}"`
THEN=`/bin/date --date="last week" +"${TIMEFMT}"`

plot_graph "weekly" "temp"     "degree Celsius (°C)" "Temperature ${NAME}" 2
plot_graph "weekly" "humidity" "humidity (%)"        "Humidity ${NAME}"    3