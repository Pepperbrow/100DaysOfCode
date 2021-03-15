# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:00:45 2021

@author: peppe
"""
#Intro to networking, Charles Severance
#net-intro.com
#Sockets like handsets for phone
#ports are like extensions (i.e. for blah-blah, please dial 4)

import socket # module gives access to TCP sockets

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


#Strings
print(ord('G')) #Gives ASCII location.  Useful with sorting.
#ASCII is simple, based on Western language
#Unicode is complex character set that caters for all languages.
