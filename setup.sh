#!/usr/bin/env bash

mkdir -p ~/.aw
cp sound/alarm.mp3 ~/.aw/
cp -r docs ~/.aw/

if [[ ! -d "~/bin" ]]; then
    mkdir -p ~/bin
fi
cp aw.py ~/bin/

exit 0
