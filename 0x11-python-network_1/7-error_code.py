#!/usr/bin/python3
"""This script retrieves the status code of a website provided as a
command-line argument. If the request fails due to an HTTP error, it prints
the error code.
"""
import requests
import sys


if __name__ == "__main__":

    target_url = sys.argv[1]
    try:
        response = requests.get(target_url)
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.status_code))
