#!/bin/bash
# Deletes content at a URL. Provide the URL as the first argument.
curl -s "$1" -X DELETE
