#!/usr/bin/env python3

"""Afterwards (aw).

See the README in docs/ or
https://github.com/trk9001/afterwards

This is in development. Intended usage:
<aw date time [-r minutes] text>

"""

import re
import sys
from subprocess import call
from textwrap import dedent

arg_i = 0  # Global index for sys.argv


def extract_date():
    """Extract the date from the command line and return it."""

    global arg_i

    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    date = sys.argv[arg_i]

    if date in ['today', 'tomorrow']:
        pass

    elif date in months or date in [m[:3] for m in months]:
        arg_i += 1
        date = ' '.join([date, str(int(sys.argv[arg_i]))])

    elif re.fullmatch(r'\d{1,2}[./-]\d{1,2}', date):
        for sep in './-':
            if sep in date:
                date = date.split(sep)
                break

        date = ' '.join([months[int(date[0]) - 1], str(int(date[1]))])

    else:
        date = None

    arg_i += 1
    return date


def main():
    """Main function."""

    global arg_i
    arg_i = 1

    date = extract_date()
    time = sys.argv[arg_i]

    arg_i += 1
    aw_text = ' '.join(sys.argv[arg_i:])

    cmd = '''\
    at {} {} << _AW_
    notify-send "{}"
    _AW_'''

    cmd = dedent(cmd.format(time, date, aw_text))
    print(cmd)
    # call(cmd, shell=True)


if __name__ == '__main__':
    main()
