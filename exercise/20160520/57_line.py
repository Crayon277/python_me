#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 57_line.py
# Created Time: Fri May 20 15:25:09 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#画图，学用line画直线。

import Tkinter
from Tkconstants import *
tk=Tkinter.Tk(className='draw line')

frame=Tkinter.Frame(tk,relief=RIDGE,borderwidth=5)

frame.pack(fill=BOTH)

canvas = Tkinter.Canvas(frame,width=800,height=600,bg='red')

canvas.pack(fill=BOTH,expand=YES)
canvas.create_line(0,0,800,600,fill='yellow',width=10)

tk.mainloop()

