#!/usr/bin/env bash

msgFile="$1"

(sleep 0.6; play -q ~/aw/sounds/alarm.mp3) &

env DISPLAY=:0.0 \
zenity --text-info \
       --title="Reminder" \
       --filename="$msgFile" \
       --html --width=500 --height=175

killall play
rm "$msgFile"
