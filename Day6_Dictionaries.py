# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:06:49 2021

@author: peppe
"""
#lists stay in order
#dictionaries are bags of values with labels
#also called associative arrays

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2

counts = dict() # new dictionary
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] # strings we want to count
for name in names:
    if name not in counts: #i.e. new name
        counts[name] = 1
    else: # already exists
        counts[name] = counts[name] + 1
print(counts)
    

if name in counts:
    x = counts[name]
else:
    x = 0
    
x = counts.get(name, 0)

counts = dict() #create empty dictionary called counts
names  = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] # strings we want to count
for name in names:
    counts[name] = counts.get(name, 0) + 1



    
counts = dict() # new dictionary
print('Enter a line of text:') # prompt
line = input('') # put input into variable

words = line.split() # split out line into new variable

print('Words:', words) # print split

print('Counting...') # print
for word in words: # loop each split in words variable
    counts[word] = counts.get(word,0) + 1 # start at 0, add 1 each time word is found
print('Counts', counts) # print results

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items(): # items gives key-value pairs
    print(aaa,bbb)

