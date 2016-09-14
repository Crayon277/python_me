#!/usr/bin/python
#-*- coding: utf-8 -*-

if __name__ == '__main__':
    from Tkinter import *
    x = 360
    y = 160
    top = x - 30
    bottom = y - 30
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    for i in range(20):
        canvas.create_oval(250-top,250-bottom,250+top,250+bottom)
        top-=5
        bottom+=5
    canvas.pack()
    mainloop()

#这个椭圆是怎么变化的要注意，从圆变上下长的扁椭圆，左上角的坐标，x是变大，y是变小
#右下角的x是变小，y是变大。是跟一开始的对比！！
