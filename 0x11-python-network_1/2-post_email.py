#!/usr/bin/python3
'''
sends a POST request to the passed URL with the email as a parameter
argv[1]: URL
argv[2]: email
'''
import urllib.request
import sys
import urllib.parse
if __name__ == '__main__':
    data = {
        'email': sys.argv[2]
    }
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode("utf-8")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read())
