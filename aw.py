#!/usr/bin/env python3

"""./aw.py 07/08 1350 notify-send Hello"""

import sys  # for command line args
import subprocess as sp  # for system calls
from textwrap import dedent  # for proper multiline string indentation


def month(n):
    """Return month name for the number"""
    if not isinstance(n, int):
        n = int(n)

    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    return months[n];


if __name__ == '__main__':
    tdate = sys.argv[1]
    tdate = tdate.split(tdate[2])
    tdate = [month(tdate[0]), str(int(tdate[1]))]
    tdate = ' '.join(tdate)

    ttime = list(sys.argv[2])
    ttime.insert(2, ':')
    ttime = ''.join(ttime)

    ttext = ' '.join(sys.argv[3:])

    cmd = '''\
    at {} {} << MARK
    {}
    MARK'''

    cmd = dedent(cmd.format(ttime, tdate, ttext))
    sp.call(cmd, shell=True)
