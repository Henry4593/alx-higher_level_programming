#!/usr/bin/python3
"""This script fetches the response from a specified URL using the Requests
library and prints details about the response body.
"""
import requests


if __name__ == "__main__":

    target_url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(target_url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
