#!/usr/bin/python3
"""queries the Reddit API """
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = 'Google Chrome Version 119.0.6045.105'

    headers = {"User-Agent": user_agent}
    params = {'limit': 10}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data")
        result = data.get("children")
        for post in result:
            print(post["data"]["title"])
    else:
        print("None")
        return
