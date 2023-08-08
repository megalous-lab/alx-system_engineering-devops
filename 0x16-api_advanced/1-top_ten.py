#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    header = {'User-Agent': 'fake'}
    param = {'limit': 10}
    r = requests.get('http://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     headers=header,
                     params=param)
    if r.status_code == requests.codes.ok:
        posts = r.json().get('data').get('children')
        for post in posts:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
