#!/usr/bin/python3
"""
Searche for a user based on a letter provided as an argument.
"""
import requests
import sys


if __name__ == "__main__":
    # Check if an argument is provided, if not, set q to an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL and data payload
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    # Send a POST request to the URL with the data payload
    response = requests.post(url, data=data)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(
                json_response.get("id"),
                json_response.get("name")
                ))

        else:
            # If the JSON is empty, display "No result"
            print("No result")
    except ValueError:
        # If the JSON is invalid, display "Not a valid JSON"
        print("Not a valid JSON")
