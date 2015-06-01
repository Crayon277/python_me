#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: gui.py
# Created Time: Wed May 13 16:34:00 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text = 'Hello , world!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text = "Hello",command = self.Hello)
        self.alertButton.pack()
        self.quitButton = Button(self,text = 'Quit', command = self.quit)
        self.quitButton.pack()
    def Hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo("Message","Hello,%s"%name)


app = Application()
app.master.title("hello GUI programming")
app.mainloop()

