#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: my_gui.py
# Created Time: Wed May 13 22:29:36 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


from Tkinter import *
import tkMessageBox
class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.numInput = Entry(self)
        self.numInput.pack()
        self.addLabel = Label(self,text = '+')
        self.addLabel.pack()
        self.num2Input = Entry(self)
        self.num2Input.pack()
        self.alertButton = Button(self, text = 'Result',command =self.calc)
        self.alertButton.pack()
        self.quitButton = Button(self,text = 'Quit', command = self.quit)
        self.quitButton.pack()
    def calc(self):
        op1 = int(self.numInput.get())
        op2 = int(self.num2Input.get())

        tkMessageBox.showinfo("Result","  %d\n+%d\n%d"%(op1,op2,op1+op2))

app = Application()
app.master.title("My gui calculating ")
app.mainloop()



