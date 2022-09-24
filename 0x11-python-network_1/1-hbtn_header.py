#!/usr/bin/python3

"""
get req header
"""

from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
