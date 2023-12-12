#!/usr/bin/python3
"""
A recursive Reddit API function fetching titles of hot articles for a subreddit, returning None if no results.
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Provides a list containing the titles of all hot articles
    for a given subreddit"""
    try:
        r = get('https://www.reddit.com/r/{}/hot.json?limit=100&&'
                'after={}'.format(subreddit, after),
                headers={'User-Agent': 'bc'})
        subreddit_dict = r.json()

        for i in range(len(subreddit_dict['data']['children'])):
            hot_list.append(subreddit_dict['data']['children'][i]
                            ['data']['title'])

        after = subreddit_dict['data']['after']

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except:
        return None
