# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:00:34 2021

@author: peppe
"""
#To change type, cast by adding int()
x = int(input('Please provide number'))
if x < 10:
    print('Smaller')
if x == 11:
    print('your number was 11')
if x <= 19:
    print('your number was less than or equal to 19')
if x >= 20:
    print('Bigger')
print('finis')

type(x)

#NOTE: Do not use tab!  Use 4 spaces.  Python can get confused.

#try/except
#If someone enters something crazy, you can catch and run something else
#only put the singl line of code that is risky in the try

#def = define function.  Reusable code snippet.
def thing():
    print('Hello')
    print('World!')
    
thing()
print('Zip')
thing()


