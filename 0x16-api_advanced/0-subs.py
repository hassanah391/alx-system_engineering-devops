#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyUserAgent/1.0'}

    response = requests.get(URL, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get('data', {}).get('subscribers', 0)
