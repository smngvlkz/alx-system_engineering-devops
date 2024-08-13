#!/usr/bin/python3
"""Counts occurrences of keywords in Reddit hot post titles."""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): The pagination token for the next page.
        word_count (Counter): Counter object to keep track of word occurrences.

    Returns:
        None: Prints the results or nothing if no matches or invalid subreddit.
    """
    if word_count is None:
        word_count = Counter()

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
                title = post['data']['title'].lower()
                update_word_count(title, word_list, word_count)


            after = data['data']['after']
            if after:

                return count_words(subreddit, word_list, after, word_count)
            else:

                print_results(word_count)
        elif response.status_code == 404:

            return
        else:

            return
    except requests.RequestException:

        return


def update_word_count(title, word_list, word_count):
    """
    Updates the word count based on the title and word list.

    Args:
        title (str): The lowercased title of a post.
        word_list (list): List of keywords to count.
        word_count (Counter): Counter object to update.
    """
    for word in word_list:
        word = word.lower()
        count = len(re.findall(r'\b{}\b'.format(re.escape(word)), title))
        if count > 0:
            word_count[word] += count


def print_results(word_count):
    """
    Prints the results in the specified format.

    Args:
        word_count (Counter): Counter object with word counts.
    """

    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))


    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
