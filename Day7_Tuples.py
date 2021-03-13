# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:20:04 2021

@author: peppe
"""
#Tuples like lists, but immutable.

#lists []
#Tuples ()
#Dictionaries {}

#Tuples more efficient than lists to store stuff you won't change

l = list()
dir(1)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

t = tuple()
dir(t)
['count', 'index']

d = {'a':10, 'b':1, 'c':22}
t  =sorted(d.items())
t
[('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items()):
    print(k,v)
    
    
# This example takes a dictionary, chucks it in a list, then reverse sorts    
c =  {'a': 20, 'b': 12, 'c': 44, 'd': 57}
tmp = list()
for k, v in c.items():
    tmp.append( (v,k) )
    
tmp = sorted(tmp, reverse=True)

