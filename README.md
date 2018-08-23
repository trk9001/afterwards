## Afterwards (aw)

[![GitHub license][2-img]][2-lnk]
![GitHub repo size in bytes][3-img]
![GitHub tag][4-img]
[![Build Status][1-img]][1-lnk]
[![codecov][6-img]][6-lnk]
![GitHub last commit][5-img]

[1-img]: https://travis-ci.com/trk9001/afterwards.svg?branch=master
[1-lnk]: https://travis-ci.com/trk9001/afterwards
[2-img]: https://img.shields.io/github/license/trk9001/afterwards.svg
[2-lnk]: https://github.com/trk9001/afterwards/blob/master/LICENSE.txt
[3-img]: https://img.shields.io/github/repo-size/trk9001/afterwards.svg
[4-img]: https://img.shields.io/github/tag/trk9001/afterwards.svg
[5-img]: https://img.shields.io/github/last-commit/trk9001/afterwards.svg
[6-img]: https://codecov.io/gh/trk9001/afterwards/branch/master/graph/badge.svg
[6-lnk]: https://codecov.io/gh/trk9001/afterwards

*Afterwards* is a command-line task reminder utility for Linux, written
primarily in Python (and utilizing Linux tools). The user specifies a date,
a time and a message, and at the specified moment *aw* sounds an alarm and
displays an alert window. That's loyalty for you.

Note that *aw* is meant to be used from the Run Command tool (usually
accessed by pressing Alt-F2 on Gnome desktops), but you can certainly run it
from the terminal as well.

### Usage

```
$ aw <date> <time> <msg>
```

- **\<date\>**:  
Supported formats:  
&nbsp;&nbsp;&nbsp;&nbsp;\- numerical (MM/DD, MM-DD, MM.DD)  
&nbsp;&nbsp;&nbsp;&nbsp;\- text (MONTH D), eg. "July 6" or "Jul 6"  
&nbsp;&nbsp;&nbsp;&nbsp;\- "today", "tomorrow"

- **\<time\>**:  
Supported formats:  
&nbsp;&nbsp;&nbsp;&nbsp;\- 24-hour (HHMM)  
&nbsp;&nbsp;&nbsp;&nbsp;\- 12-hour with AM/PM (HH:MM AM/PM)

- **\<msg\>**:  
The actual text of the reminder.  
Case sensitive (duh!).

### Dependencies

Note that so far *Afterwards* has been tested on Ubuntu 18.04 only. If you're
on it too, you would install these things by typing something like this into
your shell:  
```bash
$ sudo apt install sox libsox-fmt-mp3 zenity at
```

- **Python**:  
&nbsp;&nbsp;Surprised? Let me explain. The entire thing is written in it.  
&nbsp;&nbsp;Versions 3.5+ should work.

- **SoX**:  
&nbsp;&nbsp;*Sound eXchange, the Swiss Army knife of audio manipulation*  
&nbsp;&nbsp;(that's from the man page, but I only use it to play music).

- **libsox-fmt-mp3**:  
&nbsp;&nbsp;An MP3 handler library for SoX.

- **Zenity**:  
&nbsp;&nbsp;GTK+ dialog box maker.

- **at**:  
&nbsp;&nbsp;Non-recurring, one-time task scheduler (among other things).

### Installation

```bash
$ # Clone it from GitHub
$ git clone https://github.com/trk9001/afterwards.git
$ cd afterwards
$ # Make the setup script executable
$ chmod +x install.sh
$ ./install.sh
```

On the other hand, uninstalling is totally ez:  
```
$ aw --uninstall
```

### Testing

Use [pytest](https://pytest.org).

### The future

Can't see it.

### The *tentative* future

I was thinking of these at points:

- Easier user customization, and more of it.
- Multiple reminders for the same task. Or at least two.

### To contribute or not to contribute

If you're using *aw*, I would really appreciate your feedback and/or
criticism. And if you find it useful, please Star it!

Please check the [issues](https://github.com/trk9001/afterwards/issues) out,
and if you can help out with any, kindly make a pull request. You are also most
welcome to open an issue to report a bug or ask a q or just to chat :)

### License

Copyright © 2018 trk9001

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

### And btw

This was made for my best friend, **Shahidi**.
