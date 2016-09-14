#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 58_rectangle.py
# Created Time: Fri May 20 15:57:36 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#画方形


from Tkinter import *

tk = Tk()
tk.title('draw rectangle')

canvas = Canvas(tk,width=800,height=600,bg='blue')

#test

canvas2 = Canvas(tk,width=100,height=100,bg='yellow')

canvas.pack(expand=YES)
canvas2.pack(expand=YES)
#如果不pack就不会显示这个canvas实例

canvas.create_rectangle(200,200,500,500,fill='red',width=0)
canvas2.create_oval(0,0,100,100,fill='green')

mainloop()
