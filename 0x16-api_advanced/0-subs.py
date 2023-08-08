#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    '''return the number of subscribers'''
    url = 'https://www.reddit.com/r/{}/about.json'
    header = {'user-agent': 'myapp'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code == 404:
        return 0
    return(r.json().get('data').get('subscribers'))
