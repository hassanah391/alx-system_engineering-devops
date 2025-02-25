#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the top ten hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the top ten hot post titles for a given subreddit.
    Prints None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyUserAgent/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])

    if not data:
        print(None)
        return

    for post in data:
        print(post.get('data', {}).get('title', ''))
