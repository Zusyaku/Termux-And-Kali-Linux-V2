# Contributor(s): nigella (@nig)

from re import findall
from sys import argv, exit
from urllib.request import urlopen

__author__ = 'D4Vinci'

def get(twitter):
    ''' get information of given twitter account link or username '''

    try:
        data = urlopen(twitter).read()
        s = data.decode('utf-8')
        details = []

        [details.append(value) for value in findall('data-is-compact="false">(.*?)<', s)]

        following = details[1]
        name      = findall(b'<title>(.*?) \(', data)[0].decode('utf-8')
        tweets    = details[0]
        followers = details[2]
        likes     = details[3]
        pic       = findall(b'href="https://pbs.twimg.com/profile_images(.*?)"', data)[0].decode('utf-8')
        date      = findall(b'<span class="ProfileHeaderCard-joinDateText js-tooltip u-dir" dir="ltr" title="(.*?)"', data)[0].decode('utf-8')

        print('''
        Name: {0}
        Tweets: {1}
        Following: {2}
        Followers: {3}
        Likes: {4}
        Account made in: {5}
        Full profile picture: {6}
        '''.format(name, tweets, following, followers, likes, date, pic))

    except: print("Error <twitter_profile_link>/<username> is not correct!"); exit(0)


try: u = argv[1]
except: print(" [*] Usage: python(3) twitter_info.py <twitter_profile_link>/<username>"); exit(0)


if "twitter.com" not in u: get("http://twitter.com/" + u)
else: get(u)
