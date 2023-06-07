#!/usr/bin/python3
"""
Module contains a function that queries the Reddit API
and returns the list of all hot posts given for subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Fetches the top ten hot posts in a subreddit.
    subreddit: subreddit to fetch the top ten hot posts in a subreddit from.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if page is not None:
        url = url + "?after={}".format(page)
        headers = {
                "Users-Agent": "Chrome/91.0.4472.124"
                }
    response = requests.get(url, headers=headers, timeout=10)
    json_response = response.json()
    data = json_response.get("data")

    if response.status_code == 200:
        hot_posts = data.get("children")
        for post in hot_posts:
            hot_list.append(post.get("data").get("title"))
        page = data.get("data")
        if page is None:
            return hot_list
        return recurse(subreddit, hot_list, page.get("after"))
    else:
        return None
