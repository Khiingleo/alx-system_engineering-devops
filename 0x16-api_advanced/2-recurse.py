#!/usr/bin/python3
""" recursive function that queries reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list contianing the title of all hot articles
    for the given subreddit.
    returns None if no results are given
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "Google Chrome Version 119.0.6045.105'"

    headers = {"User-Agent": user_agent}
    params = {"limit": 100}
    if after:
        params['after'] = after

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
        posts = data.get("children")
        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data.get("after")
        if after:
            # recursively call the function with after parameter to
            # fetch next page
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
