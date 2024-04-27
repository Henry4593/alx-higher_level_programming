#!/usr/bin/python3
"""This script fetches the X-Request-Id header from a specified URL."""


import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
