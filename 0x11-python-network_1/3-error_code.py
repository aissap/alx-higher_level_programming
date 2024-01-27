#!/usr/bin/python3
"""
This script sends a request to a URL and displays the response body.
If there's an error, it prints the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Try to open the URL and get the response
    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')
            # Print the response body
            print(body)
    # If there's an HTTPError, print the error code
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
