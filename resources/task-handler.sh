#!/usr/bin/env bash

msgFile="$1"

zenity --text-info \
       --title="Reminder" \
       --filename=$msgFile \
       --html --width=500 --height=175 \
       > /dev/null 2>&1

play ~/.aw/sounds/alarm.mp3 trim 0 3
