#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: password.py
# Created Time: Wed May 13 11:40:44 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import hashlib

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

db = {

        'michael': 'e10adc3949ba59abbe56e057f20f883e',
        'bob': '878ef96e86145580c38c87f0410ad153',
        'alice': '99b1c2188db85afee403b1536010c2c9',
        'crayon':'0f7ea6416631d4acdc5e5cfe1af6f523'

}

def login(user,password):
    
    pass_md5 = calc_md5(password)
    if db[user] == pass_md5:
        print "Login sucessful"
    else:
        print "Password Denial"

if __name__ == '__main__':
    user = raw_input('usr name: ')
    if not db.has_key(user):
        print "No user %s" %user
        raise SystemExit,0
    password = raw_input("password: ")
    login(user,password)


    

