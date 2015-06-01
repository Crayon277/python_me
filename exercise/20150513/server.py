#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: server.py
# Created Time: Wed May 13 23:32:00 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import socket
import threading
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',5277))

s.listen(5)

print "waiting for connection..."




def dosomething(sock,addr):
    print "Accept new connection from %s : %s"%addr

    sock.send("Welcome")
    while 1:
        data = sock.recv(1024)
        time.sleep(1)
        if data == "exit" or not data:
            break
        sock.send("hello,%s"%data)
    sock.close()
    print 'Connecton from %s:%s closed'%(sock,addr)

if __name__ == '__main__':
    while True:
        sock, addr = s.accept()

        t = threading.Thread(target = dosomething, args = (sock,addr))
        t.start()
