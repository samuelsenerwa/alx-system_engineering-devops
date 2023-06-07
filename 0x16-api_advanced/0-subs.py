#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
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
            "user-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
            }
    response = requests.get(url, headers=headers, timeout=10)
    json_response = response.json()
    data = json_response.get("data")

    if response.status_code == 200:
        return data.get("subscribers")
    else:
        return 0
