#!/usr/bin/env python3

"""Afterwards (aw): a task reminder utility for Linux.

Copyright © 2018 trk9001

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For more information visit:
https://github.com/trk9001/afterwards
"""

import getpass
import re
import sys

import calendar as cal
import subprocess as sp
import textwrap as tw

from os import listdir
from os.path import isfile, join


class AwArgumentParser:
    """Methods to parse the command line arguments.

    Attributes:
        arg_i: Index to keep track of the arguments

    """

    def __init__(self):
        self.arg_i = 0

    def parse_for_date(self):
        """Parse the arguments for a date and return it in a known format."""

        self.arg_i += 1
        date = sys.argv[self.arg_i].lower()

        # Acceptable relative dates
        if date in ['today', 'tomorrow']:
            pass

        # Dates in words (January 1, Dec 31 etc.)
        elif date in list(cal.month_name) + list(cal.month_abbr):
            self.arg_i += 1
            date = ' '.join([date, str(int(sys.argv[self.arg_i]))])

        # Numeric dates
        elif re.fullmatch(r'\d{1,2}[./-]\d{1,2}', date):
            for sep in './-':
                if sep in date:
                    date = [int(t) for t in date.split(sep)]
                    break
            date = ' '.join([cal.month_name[date[0]], str(date[1])])

        else:
            date = None

        return date

    def parse_for_time(self):
        """Parse the arguments for a time and return it in a known format."""

        self.arg_i += 1
        time = sys.argv[self.arg_i]

        # 24-hour time
        if re.fullmatch(r'\d{4}', time):
            pass

        # 12-hour time
        elif re.fullmatch(r'\d{1,2}:\d{2}', time):
            period = sys.argv[self.arg_i + 1].upper()
            if period in ['AM', 'PM']:
                time = ' '.join([time, period])
                self.arg_i += 1

        else:
            time = None

        return time

    def parse_for_msg(self):
        """Parse the arguments for a message and return it."""

        self.arg_i += 1
        msg = ' '.join(sys.argv[self.arg_i:])
        return msg

# End of AwArgumentParser


class Aw:
    """The control centre."""

    def __init__(self):
        self.date = None
        self.time = None
        self.msg = None

    def schedule(self):
        """Call the task handler script to schedule the reminder."""

        msg_file = self.make_msg_file()

        cmd = '''\
        at {0} {1} << _AW_ > /dev/null 2>&1
        "$HOME/.aw/bin/task-handler.sh" "{2}"
        _AW_'''

        cmd = tw.dedent(cmd)
        cmd = cmd.format(self.time, self.date, msg_file)
        sp.call(cmd, shell=True)

    def make_msg_file(self):
        """Create the file from which the reminder text will be read."""

        usr = getpass.getuser()
        msg_path = '/home/' + usr + '/.aw/messages'
        msgs = [f for f in listdir(msg_path) if isfile(join(msg_path, f))]

        # Max allowed message files: 999
        if len(msgs) == 0:
            msg_file = 'msg001'
        elif msgs[-1] == 'msg999':
            msg_file = 'msg'
            for i in range(1, 999):
                msg_file += str(i).zfill(3)
                if msg_file not in msgs:
                    break
        else:
            msg_file = 'msg' + str(int(msgs[-1][3:]) + 1).zfill(3)

        # Read from the template ...
        template_file = '/home/' + usr + '/.aw/resources/msg-template'
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()

        # ... and write to the file.
        msg_file = join(msg_path, msg_file)
        with open(msg_file, 'w', encoding='utf-8') as f:
            f.write(template.format(self.msg))

        return msg_file

    def main(self):

        # Handle option to uninstall
        if '--uninstall' in sys.argv[1:]:
            sp.call('$HOME/.aw/bin/uninstall.sh', shell=True)
            return

        parser = AwArgumentParser()
        self.date = parser.parse_for_date()
        self.time = parser.parse_for_time()
        self.msg = parser.parse_for_msg()

        self.schedule()

# End of Aw


if __name__ == '__main__':

    aw = Aw()
    aw.main()
