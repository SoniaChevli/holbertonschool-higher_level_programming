#!/usr/bin/python3
'''
fetches a url
'''
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    for line in response:
        print (line)
