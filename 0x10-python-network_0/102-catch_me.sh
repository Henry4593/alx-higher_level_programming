#!/bin/bash
# Trigger specific server response on a custom URL. Provide URL as argument 1.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
