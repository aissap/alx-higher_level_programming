#!/usr/bin/python3
"""
This program takes a website URL, sends a request to it, and shows the value
of the X-Request-Id found in the response header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Open the URL and get the response
    with urllib.request.urlopen(url) as response:
        # Get the response headers
        header = response.info()
        # Print the value of the X-Request-Id header
        print(header['X-Request-Id'])
