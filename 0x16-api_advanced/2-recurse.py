#!/usr/bin/python3
"""
Recursively queries the Reddit API to retrieve all hot article titles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches all hot post titles for a given subreddit.
    Returns a list of titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}
    headers = {"User-Agent": "MyUserAgent/1.0"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        return hot_list if hot_list else None

    hot_list.extend(post["data"]["title"] for post in posts)

    after = data.get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
