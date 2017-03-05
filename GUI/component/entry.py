#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: entry.py
# Created Time: Fri Mar  3 22:56:43 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *

root = Tk()
Entry(root,text='input your text here').pack()
"""
最终效果，文本框中没有显示text，说明这个属性不是用来设置默认文本内容的。
"""

#################################################

e = StringVar()
entry = Entry(root,textvariable=e)
e.set('input your text here')
entry.pack()
"""
将变量e和entry绑定，然后将e的值设置为。。程序运行时的初始值便设置了。
"""

#################################################

e2 = StringVar()
entry2 = Entry(root,textvariable=e2,state='readonly')
e2.set('input your text here')
entry2.pack()
"""
设置entry只读，不允许用户对他的值改变。
当Entry初始化的时候没有把state参数带上的话可以后面这样写一段
entry2['state'] = 'readonly'
像是字典设置值
"""

#################################################

pwd = StringVar()
entry3 = Entry(root,textvariable=pwd)
pwd.set('input your password')
entry3.pack()
entry3['show']='*'

for mask in ['*','#','$']:
    e = StringVar()
    entry = Entry(root,textvariable=e)
    e.set('password')
    entry.pack()
    entry['show']=mask

"""
上面的就不用多说了吧，密码显示的问题
"""

#################################################

# def validate_text(contents):
    # print contents
    # return contents.isalnum()

# validate_s = StringVar()
# entry4 = Entry(root,textvariable=validate_s,validate = 'key',validatecommand=validate_text)
# validate_s.set('input your code here')
# entry4.pack()

"""
是想测试一下validate属性，但是上面这个例子有问题
"""

root.mainloop()
