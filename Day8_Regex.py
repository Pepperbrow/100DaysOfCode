# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:35:38 2021

@author: peppe
"""
import re

# re.search() check string matches regular expression
# re.findall() to extract portions of string that match regex

# This opens a file handle, removes line returns and looks for address lines
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
        
# This does same, but using regex        
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
        
# Returns list of zero or more substrings matching regex
import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)

y = re.findall('[AEIOU]+',x)

# Greedy matching - get the biggest match
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

#add ? to not be greedy
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

