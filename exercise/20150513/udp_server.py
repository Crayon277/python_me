#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: udp_server.py
# Created Time: Wed May 13 23:55:30 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",5277))


print "Bind udp on 5277"
time.sleep(5)
while 1 : 
    data , addr =  s.recvfrom(1024)
    print "connect to %s:%s"%addr
    s.sendto("welcome %s"%data,addr)
    if data == 'exit' or not data:
        break


print "connection is unlink"
