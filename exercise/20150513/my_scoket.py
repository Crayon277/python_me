#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: socket.py
# Created Time: Wed May 13 23:01:39 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('www.google.com',80))
print 'pass'
s.send('GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n')
print 'pass'
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n',1)
print header

with open('sina.html','wb') as f:
    f.write(html)


