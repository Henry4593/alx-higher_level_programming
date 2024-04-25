#!/bin/bash
# Fetch content with custom header (School ID: 98). Provide the URL as the first argument.
curl -sH "X-School-User-Id: 98" "${1}"
