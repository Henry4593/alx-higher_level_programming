#!/usr/bin/python3
"""Lists 10 most recent commits (SHA & author) for rails/rails repo."""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/repos/"
    url = url + sys.argv[2] + "/" + sys.argv[1] + "/commits"
    response = requests.get(url)
    lists_ = response.json()
    for dic in lists_[0:10]:
        print("{}: {}".format(dic.get('sha'),
                              dic.get('commit').get('author').get('name')))
