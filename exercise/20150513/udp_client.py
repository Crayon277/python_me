#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: udp_client.py
# Created Time: Wed May 13 23:55:38 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s.connect(('127.0.0.1',5277))

for x in ['Micheal','Tracy','Crayon']:
    s.sendto(x,("127.0.0.1",5277))
    print s.recv(1024)

s.close()
print "Connection break"
