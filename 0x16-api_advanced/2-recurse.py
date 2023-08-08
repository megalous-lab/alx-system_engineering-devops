#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after_party=None):
    header = {'User-Agent': 'fake'}
    param = {'after': after_party}
    r = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                     .format(subreddit, after_party),
                     headers=header)
    status = r.status_code
    if status == requests.codes.ok:
        x = r.json().get('data').get('children')
        after_party = r.json().get('data').get('after')
        for page in x:
            hot_list.append(page.get('data').get('title'))
        if len(hot_list) == 0:
            return None
        if after_party is None:
            return hot_list
        return recurse(subreddit, hot_list, after_party)
    else:
        return None
