# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:28:48 2021

@author: peppe
"""
fruit = 'banana'
index = 0
while index < len(fruit): #1st it. = 0
    letter = fruit[index] #banana. fruit[0]0 = b
    print(index, letter)  #0, b
    index = index + 1     #0+1
    
fruit = 'banana'
for letter in fruit:
    print(letter)
    
for n in 'banana':
    print(n)
    
s = 'Simon Monkey Learn Python Good'
print(s[6:25])

s = 'Simon Monkey Learn Python Good'
print(s[:25])

s = 'Simon Monkey Learn Python Good'
print(s[6:])

fruit = 'banana'
'n' in fruit
if 'a' in fruit:
    print('FOUND!')
    
#string objects have methods.
print('HI THERE!!!'.lower())

stuff = 'Hellow World'
type(stuff) # returns type of variable
dir(stuff)  # returns directory of what operaotrs are allowed

greet = 'Hello Simon'
nstr = greet.replace('Simon', 'Sarah')
print(nstr)
print (greet)

greet = '  Hi-yaaaaa  '
greet.lstrip()             #rstrip and strip also available
                           #also gets rid of /n for rstrip
#opening files

fhand = open('file.txt') # stores the file handle in variable

stuff = 'Hello\nWord' # \n adds new line. \n is one char.
stuff
print(stuff)

xfile = open('file.txt') #this code opens a file handle, then prints each line of the text file
for cheese in xfile:
    print(cheese)

#quit() terminates the program

