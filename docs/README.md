# Afterwards (aw)

*Afterwards* is a command-line task reminder utility for Linux, written
primarily in Python (but with some Bash scripting). The user specifies a date,
a time and a message, and at the specified moment *aw* sounds an alarm and
displays an alert window. That's loyalty for you.

## Usage

```
aw date time msg
```

**date**:  
In the short numerical format (MM/DD, MM-DD, MM.DD) or the word (Idk what else
to call it) format (MONTH DD) like July 6 (can take the short 3-letter form of
MONTH). Also supports 'today' and 'tomorrow'. Case insensitive. 

**time**:  
Time in the 24-hour format or AM/PM format (HH:MM AM/PM). Case insensitive.

**msg**:  
The actual text of the reminder. Case sensitive (duh!).

## Dependencies

Please install these Linux things before using *Afterwards*, otherwise your
computer will break and horrible things will happen to you:

**Python**:  
Surprised? Let me explain. The entire thing is written in it.
Versions 3.5+ should work.

**at**:  
Non-recurring, one-time task scheduler (among other things).

**Zenity**:  
GTK+ dialog box maker.

**SoX**:  
*Sound eXchange, the Swiss Army knife of audio manipulation* (that's
from the man page, but I only use it to play music).

**libsox-fmt-mp3**:  
An MP3 handler library for SoX.

## Installation

Do these things to your Bash shell:

```bash
git clone https://github.com/trk9001/afterwards.git
cd afterwards
chmod +x setup.sh
./setup.sh
```

Tada!

## The future

Can't see it.

## The tentative future

I was thinking of these at points:

- Easier user customization, and more of it.
- Multiple reminders for the same task. Or at least two.
- I want to maybe truly package it some day, like for PyPI.

## To contribute or not to contribute

If you're using ***aw***, I would really appreciate your feedback and/or
criticism. And if you find it useful, please Star it!

Please check the [issues](https://github.com/trk9001/afterwards/issues) out,
and if you can help out with any, kindly make a pull request. You are also most
welcome to open an issue to report a bug or ask a Q or just to chat :)

## License

Copyright © 2018 trk9001

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

## And btw

This was made for my best friend, **Shahidi**.