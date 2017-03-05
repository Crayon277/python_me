#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: scrollbar.py
# Created Time: Thu Mar  2 20:08:59 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill = Y)
#如果没有fill=Y的话，右边只显示了一段小框，但是没有滚动条，fill大概意思就是整条Y都填充
scrollbar_x = Scrollbar(root,orient = 'horizontal')
"""
I presume you want the "x" scrollbar to be horizontal rather than vertical. If that is true, you must tell tkinter that by using the orient option:
    
    scrollbar_x = Scrollbar(root, orient="horizontal")

"""
scrollbar_x.pack(side = BOTTOM,fill = X)
"""
side；定义停靠在父组件的哪一边上，top(default),bottom,left,right
fill: 填充x(y)方向上的空间，当属性side="top"或者"bottom"的时候填充x方向，当left或right的时候填充y方向，expand选项
      为yes，填充父组件的剩余空间
expand: 当值为yes时，side选项无效。组件显示在父配件中新位置？？？
"""
mylist = Listbox(root,xscrollcommand = scrollbar_x.set,yscrollcommand = scrollbar.set)
"""
To connect a scrollbar to another widget w, set w's xscrollcommand or yscrollcommand to the scrollbar's set() method. The arguments have the same meaning as the values returned by the get() method.
其实是因为scrollbar是双向communication，当我鼠标在listbox里面滚动的时候，这时候scrollbar也要跟着动，就要set它
"""
for line in range(100):
    mylist.insert(END,("this is line number"+str(line))*100)

mylist.pack(side = LEFT,fill=BOTH)
#这里参数中有没有fill=BOTH不一样在于，自己看
scrollbar.config(command = mylist.yview)
scrollbar_x.config(command = mylist.xview)
"""
这两句什么意思？？？
mylist.yview 
Query and change the vertical position of the view

????

为什么底部没有显示滑动条？？？
"""
"""
Scrollbars require two-way communication. The listbox needs to be configured to know which scrollbar to update when it has been scrolled, and the scrollbar needs to be configured such that it knows which widget to modify when it is moved.

When you do scrollbar.config(command=mylist.yview) you are telling the scrollbar to call the function mylist.yview whenever the user tries to adjust the scrollbar. The .yview method is a documented method on the Listbox widget (as well as a few others). If you do not set the command attribute of a scrollbar, interacting with the scrollbar will have no effect.
"""

print root.pack_slaves()
mainloop()
