#!/usr/bin/python3
"""
Send a request to a URL and displays the response body.
If the HTTP status code is 400 or higher, it prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the status code is 400 or higher
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        # Print the response body
        print(response.text)
