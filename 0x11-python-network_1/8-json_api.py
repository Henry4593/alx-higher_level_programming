#!/usr/bin/python3
"""Searches users (http://0.0.0.0:5000/) by initial letter (arg).
Prints user info (ID, name) or "No result"/errors.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    r = requests.post(url, data=payload)
    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
