#!/usr/bin/python3
'''
takes in a string
sends a search request to the Star Wars API
'''
import requests
import sys
if __name__ == '__main__':
    r = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    x = r.json()
    print('Number of results: {}'.format(x['count']))
    for i in x['results']:
        print(i['name'])
