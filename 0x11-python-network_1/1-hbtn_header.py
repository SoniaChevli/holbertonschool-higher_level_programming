#!/usr/bin/python3
'''
takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id
'''
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    headers = response.info()
    print(headers['X-Request-Id'])
