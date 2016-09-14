#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 56_circle.py
# Created Time: Fri May 20 13:55:58 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#画图，学用circle画圆形。

if __name__ == '__main__':
    from Tkinter import *
    tk = Tk(className='circle')
    frame = Frame(tk)
    frame.pack(fill=BOTH,expand=10)

    canvas = Canvas(width=800,height=600,bg='yellow')
    canvas.pack(expand=YES,fill=BOTH)

    k=1
    j=1
    for i in range(0,26):
        canvas.create_oval(310+k,250+k,310-k,250-k,width=1)
        #create_oval中的前4个参数表示两个坐标点，有这两个坐标点确定一个矩形，由这个矩形确定一个oval
        k+=j
        j+=0.3
        #增加增量

    mainloop()
