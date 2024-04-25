#!/bin/bash
# Check website health! Enter the URL as the first argument. This script shows the status code only.
curl -so /dev/null -w "%{http_code}" "$1"
