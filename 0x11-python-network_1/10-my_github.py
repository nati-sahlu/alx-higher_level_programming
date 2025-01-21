#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password) and uses the Github API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("None")

