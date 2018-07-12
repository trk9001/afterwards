#!/usr/bin/env bash

mkdir ~/.aw
mkdir ~/.aw/docs ~/.aw/sounds ~/.aw/resources ~/.aw/messages ~/.aw/bin

cp -r docs ~/.aw/
cp sounds/alarm.mp3 ~/.aw/sounds
cp resources/msg-template ~/.aw/resources/
cp -r bin ~/.aw/

chmod +x ~/.aw/bin/*

if [[ ! -d "~/bin" ]]; then
    mkdir ~/bin
fi

ln -s ~/.aw/bin/aw.py ~/bin/aw

exit 0
