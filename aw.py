#!/usr/bin/env python3

"""Afterwards (aw).

A (planned) task reminder utility for Linux.

This script is in development. Its intended usage is as follows:
`aw date time [-r minutes] text`

"""

import re
import sys
import calendar as cal
from subprocess import call
from textwrap import dedent


class AwExtractor(object):
    """A class of methods to extract data from command line arguments."""

    def __init__(self):
            self.arg_i = 0

    def extract_date(self):

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

    def extract_time(self):

            self.arg_i += 1
            time = sys.argv[self.arg_i]

            if re.fullmatch(r'\d{4}', time):
                pass

            elif re.fullmatch(r'\d{1,2}:\d{1,2}', time):
                period = sys.argv[self.arg_i + 1].upper()
                if period in ['AM', 'PM']:
                    time = ' '.join([time, period])
                    self.arg_i += 1

            else:
                time = None

            return time

# End of AwExtractor


def main():

    awe = AwExtractor()
    date = awe.extract_date()
    time = awe.extract_time()

    # hack, but TODO: rewrite without using arg_i
    text = ' '.join(sys.argv[(awe.arg_i + 1):])

    cmd = '''\
    at {} {} << _AW_
    notify-send "{}"
    _AW_'''

    cmd = dedent(cmd.format(time, date, text))
    call(cmd, shell=True)


if __name__ == '__main__':
    main()
