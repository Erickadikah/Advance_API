#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "MyBot/1.0"
            }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return None
"""
In this example, the function takes a subreddit parameter and makes a GET request to the /r/{subreddit}/about.json endpoint. The User-Agent header is used to identify the client making the request, and is required by the Reddit API. The response from the API is in JSON format, which can be parsed using the json() method of the response object. The number of subscribers is then retrieved from the data field in the JSON response.
"""
