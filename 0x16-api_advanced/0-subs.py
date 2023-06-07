#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
if there are no invalid users returns 0
"""
import requests


def number_of_subscribers(subreddit):
    """
     Fetches the number of total subscribers.
    subreddit: subreddit to fetch the number fo subscribers from.
    Return: number of subscribers or 0 if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "user-Agent": "Chrome/91.0.4472.124"
            }
    response = requests.get(url, headers=headers, timeout=10)
    json_response = response.json()
    data = json_response.get("data")

    if response.status_code == 200:
        return data.get("subscribers")
    else:
        return 0
