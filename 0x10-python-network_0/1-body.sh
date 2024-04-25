#!/bin/bash
# Snag webpage content (redirects OK). Only shows response if successful (code 200).
curl -Ls "$1"
