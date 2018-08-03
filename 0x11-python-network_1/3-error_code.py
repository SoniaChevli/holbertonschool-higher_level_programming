#!/usr/bin/python3
'''
sends a request to the URL
displays the body of the response
argv[1]: URL
'''
import urllib.request
from urllib.error import URLError
import sys
if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            s = response.read()
            print(s.decode('utf-8'))
    except URLError as e:
        print('Error code: {}'.format(e.code))
