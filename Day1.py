# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:08:35 2021

@author: peppe
"""

n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')

type(n) #gives type of variable n

print(99/100) #results in 0.99

m = 'lemons'
p = 'cucumber'

m + p

nam = input('What is your name?')
print('Hello', m + nam + p)

inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)