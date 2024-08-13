#!/usr/bin/python3
"""Queries the Reddit API and print titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of the first 10 hot posts, or None for invalid subreddits.
    """

    headers = {'User-Agent': 'MyRedditBot/1.0'}


    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
