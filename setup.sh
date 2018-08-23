#! /usr/bin/env bash

mkdir -p "$HOME/.afterwards/messages"
cp -r aw "$HOME/.afterwards/"

# Remove Python packaging
rm "$HOME/.afterwards/aw/__init__.py"

# Executable scripts
chmod +x "$HOME/.afterwards/aw/afterwards.py"
chmod +x "$HOME/.afterwards/aw/bin/task-handler.sh"
chmod +x "$HOME/.afterwards/aw/bin/uninstall.sh"

# Installs to user's ~/bin
if [[ ! -d "$HOME/bin" ]]; then
    mkdir "$HOME/bin"
fi

# Symlink to the main script in ~/bin
ln -s "$HOME/.afterwards/aw/afterwards.py" "$HOME/bin/aw"

echo "Setup was successful."
exit 0
