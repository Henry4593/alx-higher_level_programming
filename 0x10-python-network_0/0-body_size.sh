#!/bin/bash
# This script fetches a URL (provided as argument), silently retrieves header info, isolates the Content-Length value, and displays it.
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
