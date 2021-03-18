# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 21:37:21 2021

@author: peppe
"""
class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

an.party()

class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

dir(PartyAnimal())

dir(an)

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam): #Constructor
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()

#Inheritance - make new class with old - extending/subclassing
#class blahblah(oldclass)

#Class = template
#Attribute = variable in class
#Method = Function in class
#Object = Instance of a class
#Constructor = code that runs when object created
#Inheritance = abiity to extend class to make new class
