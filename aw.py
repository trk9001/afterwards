#!/usr/bin/env python3

"""Afterwards (aw).

A (planned) task reminder utility for Linux.

This script is in development. Its intended usage is as follows:
`aw date time [-r minutes] text`

"""

import re
import sys
import calendar as cal
import subprocess as sp
import textwrap as tw


class AwArgumentParser:
    """Methods to parse the command line arguments."""

    def __init__(self):
        self.arg_i = 0

    def parse_for_date(self):

        self.arg_i += 1
        date = sys.argv[self.arg_i]

        if date in ['today', 'tomorrow']:
            pass

        elif date in list(cal.month_name) + list(cal.month_abbr):
            self.arg_i += 1
            date = ' '.join([date, str(int(sys.argv[self.arg_i]))])

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

        self.arg_i += 1
        time = sys.argv[self.arg_i]

        if re.fullmatch(r'\d{4}', time):
            pass

        elif re.fullmatch(r'\d{1,2}:\d{2}', time):
            period = sys.argv[self.arg_i + 1].upper()
            if period in ['AM', 'PM']:
                time = ' '.join([time, period])
                self.arg_i += 1

        else:
            time = None

        return time

    def parse_for_msg(self):

        self.arg_i += 1
        msg = ' '.join(sys.argv[self.arg_i:])
        return msg

# End of AwArgumentParser


class Aw:
    """Control centre."""

    def __init__(self):
        self.date = None
        self.time = None
        self.msg = None

    def schedule(self):

        cmd = '''\
        at {} {} << _AW_
        notify-send "{}"
        play ~/.aw/alarm.mp3 trim 0 3
        _AW_'''

        cmd = tw.dedent(cmd)
        cmd = cmd.format(self.time, self.date, self.msg)
        sp.call(cmd, shell=True)

    def main(self):

        parser = AwArgumentParser()
        self.date = parser.parse_for_date()
        self.time = parser.parse_for_time()
        self.msg = parser.parse_for_msg()

        self.schedule()

# End of Aw


if __name__ == '__main__':

    aw = Aw()
    aw.main()
