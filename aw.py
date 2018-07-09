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


_arg_i = 0  # Global index for sys.argv


def parse_date(dt):
    """A date-parser function.

    Converts a date's format from various possible ones to a single convenient
    one, and returns it.

    Args:
        dt: The date argument as read from the command line.

    """

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

    if dt in ['today', 'tomorrow']:
        pass

    elif dt in months or dt in [m[:3] for m in months]:
        global _arg_i
        dt = ' '.join([dt, str(int(sys.argv[_arg_i + 1]))])
        _arg_i += 1

    elif re.fullmatch(r'\d{1,2}[./-]\d{1,2}', dt):
        for sep in './-':
            if sep in dt:
                dt = dt.split(sep)
                break

        month_chart = dict()
        for i, month in enumerate(months):
            month_chart[i + 1] = month

        dt = ' '.join([month_chart[int(dt[0])], str(int(dt[1]))])
    
    else:
        return None

    return dt


def main():
    """Main function."""

    _arg_i += 1
    aw_date = sys.argv[_arg_i]
    aw_date = parse_date(aw_date)

    _arg_i += 1
    aw_time = sys.argv[_arg_i]

    _arg_i += 1
    aw_text = ' '.join(sys.argv[_arg_i:])

    cmd = '''\
    at {} {} << _AW_
    notify-send "{}"
    _AW_'''

    cmd = dedent(cmd.format(aw_time, aw_date, aw_text))
    call(cmd, shell=True)


if __name__ == '__main__':
    main()
