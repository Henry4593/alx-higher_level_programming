#!/usr/bin/python3
"""This script retrieves the status code of a website provided as a
command-line argument. If the request fails due to an HTTP error, it prints
the error code.
"""
import requests
import sys


if __name__ == "__main__":

    target_url = sys.argv[1]
    response = requests.get(target_url)
    
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
