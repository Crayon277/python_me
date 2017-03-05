#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: StringVar.py
# Created Time: Thu Mar  2 16:23:11 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *

def callback(*args):
    print 'variable changed!'

top = Tk()
label = Label(top,text = 'test stringvar')
label.pack()

cwd = StringVar() #StringVar(top) 有没有这里面的top一样
cwd.trace("w",callback) # trace(mode,callback) 
"""
mode
"r": call observer when variable is read by someone
"w": call when variable is written by someone
"u": undefine,call when the variable is deleted
"""
cwd.set('hahahah')
label_cwd = Label(top,text=cwd.get())
label_cwd.pack(expand = 1)
mainloop()
