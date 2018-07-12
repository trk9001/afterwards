#!/usr/bin/env bash

msgFile="$1"

(sleep 0.6; play -q ~/aw/sounds/alarm.mp3 > /dev/null 2>&1) &

zenity --text-info \
       --title="Reminder" \
       --filename="$msgFile" \
       --html --width=500 --height=175 \
       > /dev/null 2>&1

killall play
