# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:14:44 2021

@author: peppe
"""
while True:
    line = input('> ')
    if line == 'done':
        break
        print(line)
print('Done!')

#break stops the chunk of code.  continue breaks the iteration
#and takes you back to the beginning of the loop.
#while loops are 'indefinite' and will run until no longer true.

for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')

#This is a definite loop.  It loops for each item in the list.

family = ['Jonah', 'Simon', 'Dylan', 'Sarah']
for name in family:
    print('Happy New Year:', name)
print('Done!')


numbr = 0 #count variable
for n in ['20', '54', '36', '48', '92']: #numbers to iterate through
    numbr = numbr + 1 #add 1 to count for each iteration
    print(numbr, n) #print the count iteration and the list number
print('After', numbr) #at end of loop, print After (last iteration)
    