#!/usr/bin/python3
'''argv[1] a letter
post to URL
with letter set to variable q
'''
import requests
import sys

if __name__ == '__main__':

    d = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=d)

    if type(r.text) is not str:
        print('Not a valid JSON type is {}'.format(type(r)))
    elif len(r.text) == 0:
        print('No result')
    else:
        x = r.json()
        print('[{}] {}'.format(x['id'], x['name']))
