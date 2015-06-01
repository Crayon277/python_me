#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: client.py
# Created Time: Wed May 13 23:36:54 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',5277))

print s.recv(1024)

for data in ['Micheal','Tracy','Sarah']:
    s.send(data)
    print s.recv(1024)

s.send("exit")
s.close()
