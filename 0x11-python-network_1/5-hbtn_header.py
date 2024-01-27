#!/usr/bin/python3
"""
Fetches a URL and shows the value of the X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of the X-Request-Id header and print it
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
