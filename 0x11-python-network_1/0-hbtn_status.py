#!/usr/bin/python3
'''
fetches a url
'''
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    utf8_content = response.read().decode('utf-8')
    str1 = ''
    for line in response:
        str1 += line

    print('Body response:')
    print('\t- type: <class \'bytes\'>')
    print('\t- content: %s'.format(str1))
    print('\t- utf8 content: %s'.format(utf8_content))
