#!/bin/bash
# Send a message (email & subject) via POST. Provide URL as argument 1.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
