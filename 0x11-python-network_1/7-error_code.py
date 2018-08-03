#!/usr/bin/python3
'''
argv[1]: URL
sends a request and displays body
'''
import requests
import sys
if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
