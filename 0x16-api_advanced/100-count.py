#!/usr/bin/python3
"""
Recursively queries the Reddit API, counts keyword occurrences
in hot article titles,
and prints them in descending order of frequency.
"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and counts occurrences of given keywords (case-insensitive).
    Prints sorted results based on count (descending) and alphabetically
    """
    if counts is None:
        counts = {}

    word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    headers = {"User-Agent": "MyUserAgent/1.0"}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post["data"]["title"].lower()
        words = title.split()
        for word in words:
            clean_word = ''.join(filter(str.isalpha, word))
            if clean_word in word_list:
                counts[clean_word] = counts.get(clean_word, 0) + 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, counts, after)

    if counts:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
