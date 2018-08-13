# Afterwards (aw)

*Afterwards* is a command-line task reminder utility for Linux, written
primarily in Python (and utilizing Linux tools). The user specifies a date,
a time and a message, and at the specified moment *aw* sounds an alarm and
displays an alert window. That's loyalty for you.

Note that *aw* is supposed to be used from the Run Command thing (usually
accessed by pressing Alt-F2).

## Usage

```
$ aw date time msg
```

- **date**:  
Case insensitive.  
Supported formats:
    - numerical (MM/DD, MM-DD, MM.DD)
    - text (MONTH D), eg. "July 6" or "Jul 6"
    - "today", "tomorrow"

- **time**:  
Case insensitive.  
Supported formats:
    - 24-hour (HHMM)
    - 12-hour with AM/PM (HH:MM AM/PM)

- **msg**:  
The actual text of the reminder.  
Case sensitive (duh!).

## Dependencies

Do note that so far *Afterwards* has been tested on Ubuntu 18.04 only. If you're
on it too, you would install these things by putting `sudo apt install` before
their names. Something like  
```bash
$ sudo apt install sox libsox-fmt-mp3 zenity at
```

- **Python**:  
Surprised? Let me explain. The entire thing is written in it.  
Versions 3.5+ should work.

- **SoX**:  
*Sound eXchange, the Swiss Army knife of audio manipulation*  
(that's from the man page, but I only use it to play music).

- **libsox-fmt-mp3**:  
An MP3 handler library for SoX.

- **Zenity**:  
GTK+ dialog box maker.

- **at**:  
Non-recurring, one-time task scheduler (among other things).

## Installation

```bash
$ # Clone it from GitHub
$ git clone https://github.com/trk9001/afterwards.git

$ cd afterwards

$ # Make the setup script executable
$ chmod +x setup.sh

$ ./setup.sh
```

## The future

Can't see it.

## The tentative future

I was thinking of these at points:

- Easier user customization, and more of it.
- Multiple reminders for the same task. Or at least two.
- I want to maybe truly package it some day, like for PyPI.

## To contribute or not to contribute

If you're using *aw*, I would really appreciate your feedback and/or
criticism. And if you find it useful, please Star it!

Please check the [issues](https://github.com/trk9001/afterwards/issues) out,
and if you can help out with any, kindly make a pull request. You are also most
welcome to open an issue to report a bug or ask a q or just to chat :)

## License

Copyright © 2018 trk9001

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

## And btw

This was made for my best friend, **Shahidi**.