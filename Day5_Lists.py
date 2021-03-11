# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 20:17:58 2021

@author: peppe
"""
# Algorithm is series of steps.
# Data Structures are ways to lay out data.
# Collections are suitcases - you can store multiple vars!

family = ['Simon', 'Sarah', 'Jonah', 'Dylan']

# Can mix it up:

stuff = [24, '32', 3.5, 'Blue burblers']
    
fruit = 'Banana'
fruit[0] = 'b' # dunt work!  Strings are immutable.

lotto = [92, 14, 26, 41, 63]
print(lotto)
lotto[2] = 27
print(lotto) # Lists are.

print(range(4))
friends = ['Yosef', 'Glynn', 'Sully']
print(len(friends))
print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

range(len(friends))

for friend in friends:
    print('Happy New Year:', friend)
    
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

d = [1,5,3]
e = [4,2,6]
f = d + e

f[3:5]
f[:]

# Building a list
#[]
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')

'cookie' in stuff
'vegetable' not in stuff

stuff.sort() # cannot do as mix of types.
#can have len, max, min, sum, sum/len etc. e.g.:
print(len(stuff))

# To turn a string into a list, you can use split.

abc = 'We Three Free Men'
stuff = abc.split()
print(stuff)
print(stuff[3])

# Can deliniate split by specifying e.g.
line = ('super;duper;mcpartypooper')
line.split(';')


















