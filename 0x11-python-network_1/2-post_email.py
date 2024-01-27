#!/usr/bin/python3
"""
This program sends an email to a URL using a POST request and prints the response.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request object
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and get the response
    with urllib.request.urlopen(req) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')

        # Print the decoded response body
        print(body)
