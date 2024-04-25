#!/bin/bash
# Discover allowed actions for a URL. Enter the URL as the first argument.
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
