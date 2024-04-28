#!/usr/bin/python3
"""This script sends a POST request to a URL with email data in the body."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    target_url = sys.argv[1]
    email_data = {"email": sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email_data)
    byte_data = encoded_data.encode("ASCII")
    request_object = urllib.request.Request(target_url, method="POST",
                                            data=byte_data)

    with urllib.request.urlopen(request_object) as response:
        returned_page = response.read().decode("utf-8")
        print(returned_page)
