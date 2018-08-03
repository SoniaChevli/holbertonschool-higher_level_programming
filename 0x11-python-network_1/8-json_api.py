#!/usr/bin/python3
'''argv[1] a letter
post to URL
with letter set to variable q
'''
import requests
import sys

if __name__ == '__main__':
    try:
        d = {'q': sys.argv[1]}
    except:
        d = {'q': ''}

    r = requests.post('http://0.0.0.0:5000/search_user', data=d)

    try:
        x = r.json()
        if len(x) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(x['id'], x['name']))

    except:
        print('Not a valid JSON type is {}'.format(type(r)))
