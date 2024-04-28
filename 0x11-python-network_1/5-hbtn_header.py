#!/usr/bin/python3
"""This script fetches the X-Request-Id header from a specified URL using the
Requests library.
"""
import requests
import sys


if __name__ == "__main__":

    target_url = sys.argv[1]
    response = requests.get(target_url)
    header = response.headers.get("X-Request-Id")
    print(header)
