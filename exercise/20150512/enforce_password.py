#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: enforce_password.py
# Created Time: Wed May 13 12:09:38 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import hashlib
import password as imp_pwd


def register(username,password):
    imp_pwd.db[username] = imp_pwd.calc_md5(password + username + 'the-Salt')
def login():
    user = raw_input("Enter your name: ")
    password = raw_input("Enter your password: ")

    check_md5 = imp_pwd.calc_md5(password + user + 'the-Salt')
    if imp_pwd.db.has_key(user) and imp_pwd.db[user] == check_md5:
        print "login successful"
    else:
        print "Wrong password or no user"

if __name__ == '__main__':
    
    choice = (raw_input("register or login : "))
    if choice[0].lower() == 'r':
        user = raw_input("Enter your name: ")
        password = raw_input("Set your password: ")
        register(user,password)
       # print imp_pwd.db
        login()
    else:
        user = raw_input('usr name: ')
        if not imp_pwd.db.has_key(user):
            print "No user %s" %user
            raise SystemExit,0
        password = raw_input("password: ")
        login(user,password)





