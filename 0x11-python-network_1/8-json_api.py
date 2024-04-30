#!/usr/bin/python3
"""Searches users (http://0.0.0.0:5000/) by initial letter (arg).
Prints user info (ID, name) or "No result"/errors.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    m = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = m.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
