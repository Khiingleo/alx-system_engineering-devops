#!/usr/bin/python3
"""query for the reddit api that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the reddit api
    Returns:
        the number of subscribers of the given subreddit
        0 if an invalid subreddit is given
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = 'Google Chrome Version 119.0.6045.105'
    headers = {'User-Agent': user}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        return 0
