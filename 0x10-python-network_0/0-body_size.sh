#!/usr/bin/bash
#kes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -X GET -s "$1" | wc -c
