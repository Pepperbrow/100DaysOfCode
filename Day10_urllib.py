# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:33:07 2021

@author: peppe
"""
import urllib.request, urllib.parse, urllib.error
# No headers, opens page via file handle

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    
counts = dict() # makes dictionary
for line in fhand:
    words = line.decode().split() # scans each line
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # counts each word
print(counts)

fhand = urllib.request.urlopen('http://www.bbc.co.uk/news')
for line in fhand:
    print(line.decode().strip())
    
#Beautiful Soup can be used to get HTML without having to constantly amend your code
# Install from https://pypi.python.org/pypi/beautifulsoup4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ') # asks for website to scrape
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve anchor tags
tags = soup('a') # for each href tag
for tag in tags:
    print(tag.get('href', None)) # print the tag
