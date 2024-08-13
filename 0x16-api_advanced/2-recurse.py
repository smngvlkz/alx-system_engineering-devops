#!/usr/bin/python3
"""Recursively queries the Reddit API and get all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles (used for recursion).
        after (str): The pagination token for the next page.

    Returns:
        list: A list of all hot article titles, or None if the subreddit is invalid.
    """

    headers = {'User-Agent': 'MyRedditBot/1.0'}


    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:

        response = requests.get(url, headers=headers, params=params, allow_redirects=False)


        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.RequestException:
        return None
