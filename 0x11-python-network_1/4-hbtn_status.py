#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
"""
import requests


if __name__ == "__main__":
    # Define the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the response body
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
