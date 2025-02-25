#!/usr/bin/python3
"""
Retuens number of subscribers for a passed subreddit name using reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retuens number of subscribers for a passed subreddit name using reddit API
    """
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    req = requests.get(URL, headers=headers).json()
    subscribers = req.get('data', {}).get('subscribers')
    if not subscribers:
        return 0


    return subscribers
