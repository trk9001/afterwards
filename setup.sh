#! /usr/bin/env bash

mkdir "$HOME/.aw"
mkdir "$HOME/.aw/docs" \
      "$HOME/.aw/sounds" \
      "$HOME/.aw/resources" \
      "$HOME/.aw/messages" \
      "$HOME/.aw/bin"

cp -r docs "$HOME/.aw/"
cp sounds/alarm.mp3 "$HOME/.aw/sounds"
cp resources/msg-template "$HOME/.aw/resources/"
cp -r bin "$HOME/.aw/"

chmod +x "$HOME/.aw/bin/aw.py"
chmod +x "$HOME/.aw/bin/task-handler.sh"
chmod +x "$HOME/.aw/bin/uninstall.sh"

if [[ ! -d "$HOME/bin" ]]; then
    mkdir "$HOME/bin"
fi

ln -s "$HOME/.aw/bin/aw.py" "$HOME/bin/aw"

exit 0
