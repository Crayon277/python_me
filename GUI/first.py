#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: first.py
# Created Time: Wed Mar  1 21:17:21 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top,text = 'Hello World!')
label.pack()
# label.pack(expand=1)
"""
有了expand这个参数会形成的效果是，当窗口拉大的时候，label会时刻居中显示。
"""
Tkinter.mainloop()
