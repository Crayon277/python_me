#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: frame.py
# Created Time: Thu Mar  2 17:10:00 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *

root =Tk()
frame =Frame(root)
# 参数表示父窗口
frame.pack()

bottomframe = Frame()
bottomframe.pack(side = BOTTOM)

redbutton = Button(frame,text = 'red',fg='red')
redbutton.pack(side = LEFT)

greenbutton = Button(frame,text = 'green',fg='brown')
greenbutton.pack(side=LEFT)

bluebutton = Button(frame,text='blue',fg='blue')
bluebutton.pack(side = RIGHT)

blackbutton = Button(bottomframe,text='Black',fg='black')
blackbutton.pack(side=LEFT)
mainloop()
