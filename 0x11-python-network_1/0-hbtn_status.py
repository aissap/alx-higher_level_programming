#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
and displays information about the response body.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:\n"
      f"\t- type: {type(body)}\n"
      f"\t- content: {body}\n"
      f"\t- utf8 content: {body.decode('utf-8')}")
