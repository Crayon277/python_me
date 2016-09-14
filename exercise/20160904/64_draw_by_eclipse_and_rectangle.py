#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 64_draw_by_eclipse_and_rectangle.py
# Created Time: Sun Sep  4 20:10:45 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

if __name__ == '__main__':
    from Tkinter import *
    canvas = Canvas(width=400,height=600,bg='white')
    left = 20
    right = 50
    top = 50
    num = 15

    for i in range(num):
        canvas.create_oval(250-right,250-left,250+right,250+left)
        canvas.create_oval(300,250-top,200,250+top)
        canvas.create_rectangle(0+right,0+left,250-right,250-left)
        left +=5
        right +=5
        top+=5
    canvas.pack()
    mainloop()
