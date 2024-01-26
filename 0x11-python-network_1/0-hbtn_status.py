#!/usr/bin/python3
"""
This program fetches information from a website and shows it.
"""

import urllib.request

# The URL we want to get information from
url = "https://alx-intranet.hbtn.io/status"

# Open the URL and get the response
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read()

# Display the response information
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode("utf-8"))
