#!/usr/bin/python3
"""Retrieve and print 10 commits of a repository by specific user
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the URL for the Github PI endpoint
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    # Send a GET request to the GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)
