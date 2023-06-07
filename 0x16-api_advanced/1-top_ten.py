#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            "User-Agent": "Chrome/91.0.4472.124"
            }
    response = requests.get(url, headers=headers, timeout=10)
    json_response = response.json()
    data = json_response.get("data")

    if response.status_code == 200:
        hot_posts = data.get("children")
        for post in hot_posts:
            print(post.get("data").get("title"))
    else:
        print(None)
