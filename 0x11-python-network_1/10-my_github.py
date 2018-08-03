#!/usr/bin/python3
'''
takes github cred
display id
'''
import sys
import requests
if __name__ == '__main__':
    url = 'https://api.github.com/user'
    p = {'login': sys.argv[1]}
    r = requests.get(url, params={'login': sys.argv[1]},
                     auth=(sys.argv[1], sys.argv[2])).json()

    try:
        print(r['id'])
    except KeyError:
        print('None')
