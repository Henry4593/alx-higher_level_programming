#!/usr/bin/python3
"""This script fetches a URL and prints its content, handling potential
errors.
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":

    target_url = sys.argv[1]
    try:
        with urllib.request.urlopen(target_url) as response:
            print(response.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
