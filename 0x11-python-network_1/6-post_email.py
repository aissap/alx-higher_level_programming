#!/usr/bin/python3
"""
Sends an email address to a URL using a POST request and prints the response.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the email payload
    payload = {'email': email}

    # Send a POST request to the URL with the email payload
    response = requests.post(url, data=payload)

    # Print the email address
    print("Your email is:", email)

    # Print the response body
    print(response.text)
