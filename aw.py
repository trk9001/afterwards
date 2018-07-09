#!/usr/bin/env python3

"""Afterwards (aw).

See the README in docs/ or
https://github.com/trk9001/afterwards

This is in development. Intended usage:
<aw date time [-r minutes] text>

"""

import calendar as cal
import re
import sys
from subprocess import call
from textwrap import dedent


class AwExtractor(object):
    """Methods to extract data from command line arguments."""

    def __init__(self):
            self.arg_i = 0

    def extract_date(self):
            """Extract the date from the command line and return it."""

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
            """Extract the time from the command line and return it."""


# End of AwExtractor


def main():
    """Main function."""

    awe = AwExtractor()
    date = awe.extract_date()

    time = sys.argv[(awe.arg_i + 1)]

    aw_text = ' '.join(sys.argv[(awe.arg_i + 2):])

    cmd = '''\
    at {} {} << _AW_
    notify-send "{}"
    _AW_'''

    cmd = dedent(cmd.format(time, date, aw_text))
    print(cmd)
    # call(cmd, shell=True)


if __name__ == '__main__':
    main()
