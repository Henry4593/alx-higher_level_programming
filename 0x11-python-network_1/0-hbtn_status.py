#!/usr/bin/python3
"""This script checks the status of a website and prints details about
the response.
"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf_8 = content.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf_8))
