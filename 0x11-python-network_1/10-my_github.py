#!/usr/bin/python3
"""
Use Basic Authentication with a personal access token to access GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    # Get the username and personal access token from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get('https://api.github.com/user',
                            auth=(username, password))

    # Check if the request is successful
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
