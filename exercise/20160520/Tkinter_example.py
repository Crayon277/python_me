#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: Tkinter_example.py
# Created Time: Fri May 20 14:01:41 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


import Tkinter 
from Tkconstants import *
tk = Tkinter.Tk(className='first window')
#初始一个Tk类，貌似是主窗口
frame = Tkinter.Frame(tk,borderwidth=20)
#这应该是初始一个Frame类，是一个widget,窗口部件
#在frame里面添加内容

frame.pack(fill=BOTH,expand=1)
#pack a widget in the parent widget

label = Tkinter.Label(frame,text='Hello,World')
label.pack(fill=None,expand=40)

button = Tkinter.Button(frame,text='Exit',command=tk.destroy)
button.pack(side=TOP)

tk.mainloop()
