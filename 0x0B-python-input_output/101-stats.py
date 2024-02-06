#!/usr/bin/python3
"""Processes input lines from standard input, tracking file size and status
   code counts.
"""

import sys


def print_stats():
    """Prints the current file size and counts of tracked status codes."""

    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

line_count = 0
file_size = 0

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            print_stats()

        pieces = line.split()

        try:
            status = int(pieces[-2])
            status_codes[str(status)] += 1
        except (ValueError, IndexError):
            pass

        try:
            file_size += int(pieces[-1])
        except (ValueError, IndexError):
            pass

        line_count += 1

    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
