# README

*For **beb**.*

## What I want it to be

So this is going to be like, a task reminder utility for Linux, written in Bash
or Python. Off the top of my head, it will be based on the `at` command for
Linux and may make use of a lightweight database like SQLite. It will play an
alarm at the specified time(s).

For now, the goal is to make something like this:
```
aw <date> <time> [-r mins] <task>

date
  Either an actual date like '7/5' (for July 5) or relative stuff like 'today'
  or 'tomorrow'. Maybe even weekdays.

time
  Time in 24-hour format.

-r mins
  An option to sound the alarm 'mins' minutes before the task as well.

task
  The actual task.
```

I'm thinking it might have an rc file and/or a config directory to hold any
data, database and alarm audio.

## To contribute (or not to contribute, that is the question)

Please take a look at the [Issues](https://github.com/trk9001/afterwards/issues),
and if you can help with any, please make a pull request. You are also most
welcome to open an issue to report a bug or just to chat :)
