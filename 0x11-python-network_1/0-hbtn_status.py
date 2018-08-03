#!/usr/bin/python3
'''
fetches a url
'''
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    tmp = response.read()
    utf8_content = tmp.decode('utf-8')

    print('Body response:')
    print('\t- type: {}'.format(type(tmp)))
    print('\t- content: {}'.format(tmp))
    print('\t- utf8 content: {}'.format(utf8_content))
