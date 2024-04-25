#!/bin/bash
# Send JSON data to a URL (argument 1). Provide JSON data file as argument 2.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
