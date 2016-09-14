#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 57_line_v2.py
# Created Time: Fri May 20 15:44:04 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *

canvas = Canvas(width=300,height=300,bg='green')
canvas.pack(expand=YES,fill=BOTH)

x0=263
y0=263
y1=275

for i in range(19):
    canvas.create_line(x0,y0,x0,y1,fill='red')
    x0-=5
    y0-=5
    y1+=5

x0=263
y0=263
y1=275

for i in range(10):
    canvas.create_line(x0,y0,x0,y1,fill='red')
    x0+=5
    y0+=5
    y1+=5

mainloop()
