#!/usr/bin/python3
"""This script sends a POST request to a URL with email data in the body using
the Requests library.
"""
import requests
import sys


if __name__ == "__main__":

    target_url = sys.argv[1]
    email_data = {"email": sys.argv[2]}
    response = requests.post(target_url, data=email_data)
    print(response.text)
