#!/usr/bin/env python
# coding=utf-8

'''
GUI小部件通常有很多参数，比如文本框的大小，长度，尺寸，背景颜色等等，
如果想固定其中的一些参数，如让所有的文本标签为蓝底白字，就可以准确的以
PFA的方式，自定义为相似对象的伪模版
'''

from functools import partial
import Tkinter

root = Tkinter.Tk()

myButton = partial(Tkinter.Button,root,fg='white',bg='red')

b1=myButton(text='button1')
b2=myButton(text='button2')
qb=myButton(text='quit',bg='blue',command=root.quit)

b1.pack()
b2.pack()
qb.pack(fill=Tkinter.X,expand=True)#expand 是上下会随着边框我们拉长而居中
root.title('PFA!')
root.mainloop()
