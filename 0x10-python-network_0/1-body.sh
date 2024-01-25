#!/bin/bash
# Sends a GET request to a URL and displays the body of the response for a 200 status code
curl -sL -w "%{http_code}" "$1" -o temp_response.txt | tail -n +2
