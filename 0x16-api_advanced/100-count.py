#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API and counts the occurrences
    of given keywords in hot articles.
    Prints the counts in descending order by count and alphabetically
    if counts are the same.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = 'Google Chrome Version 119.0.6045.105'

    headers = {"User-Agent": user_agent}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
        posts = data.get("children")

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word] = (counts.get(word, 0) +
                                    title.count(word.lower()))

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda item:
                                   (-item[1], item[0]))
            for keyword, count in sorted_counts:
                print("{}: {}".format(keyword, count))
    else:
        print("Invalid subreddit.")
