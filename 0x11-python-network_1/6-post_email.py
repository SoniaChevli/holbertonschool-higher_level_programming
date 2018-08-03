#!/usr/bin/python3
'''
argv[1]: URL
argv[2]: email
posts email to URL
'''
import requests
import sys
if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
