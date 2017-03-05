#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: my_listdir.py
# Created Time: Fri Mar  3 21:23:05 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from Tkinter import *
import os
import pdb
from time import sleep

class DirList(object):
    def __init__(self,initdir = None):
        self.top = Tk()
        # self.top.title = 'Directory List'
        #这个为什么不起作用
        #title是一个函数啊
        self.top.title('Directory List')
        self.version = Label(self.top,text='Derectory Lister v1.1')
        self.version.pack()
        self.cwd = StringVar(self.top,value='test')
        # value值是设置初始值
        self.dirlabel = Label(self.top,text=self.cwd.get(),font =('Helvetic',12,'bold'),foreground='blue')
        #这个text参数在这里有用吗
        self.dirlabel.pack()
        
        self.dirfm = Frame(self.top)
        self.dirscroll = Scrollbar(self.dirfm)
        self.dirlistbox = Listbox(self.dirfm,yscrollcommand = self.dirscroll.set,height = 15,width=40)
        #listbox和scrollbar相互交互
        """
        为什么显示出来的height和width差不多呢？不应该宽是长的两倍么？
        """
        self.dirlistbox.bind('<Double-1>',func = self.selectAndGo)
        self.dirscroll.config(command=self.dirlistbox.yview)

        #test
        # for i in range(1,100):
            # self.dirlistbox.insert(END,i)

        self.dirscroll.pack(side = RIGHT,fill=Y)
        self.dirlistbox.pack(side = LEFT,fill=BOTH) #这里面参数有没有区别不大啊
        self.dirfm.pack()
        
        self.dirfm2 = Frame(self.top)
        self.input = Entry(self.top,textvariable=self.cwd,width=40)
        """
        用textvariable将entry和stringvar绑定了，entry中和stringvar变量同步变动

        update :
        发现一个新的问题，输入文本框的前面的值没有被清空
        """
        self.input.bind('<Return>',func = self.doLs)
        self.input.pack()
        
        self.clear = Button(self.dirfm2,command = self.clrDir,activebackground='black',activeforeground='yellow',text='clear')
        self.clear.pack(side=LEFT)
        self.listdir = Button(self.dirfm2,command = self.doLs, activebackground='red',activeforeground='black',text='List Directory')
        self.listdir.pack(side=LEFT)
        self.quit = Button(self.dirfm2,command=self.top.quit,activebackground = 'blue',activeforeground='grey',text='QUIT')
        self.quit.pack(side=LEFT)
        """
        这几个activebackground和activeforeground不起作用
        
        the buttons on the mac simply don't support changing the background and foreground colors.

        为什么我的组件不是居中的？？？
        把Entry那个组件pack到top中，不是pack到frame中去就可以了
        """
        self.dirfm2.pack()

        if initdir:
            self.cwd.set(initdir)
            self.doLs()
    
    # def test_select(self,ev=None):
        #这个ev在这里没什么用，但是如果没有ev参数在这里会报错，可能是bind里传过来的参数的原因，深究一下。
        # self.cwd.set(self.dirlistbox.selection_get()) 
        # self.test_show()
    # def test_show(self,ev=None):
        # cur = self.cwd.get()
        # self.cwd.set('fetching...')
        # self.dirlabel.config(text=cur) 
        # self.top.update()
    def clrDir(self):
        self.cwd.set('')
        
    def selectAndGo(self,ev=None):
        #in case of error, save the last path
        self.last = self.cwd.get()
        self.dirlistbox.config(selectbackground='red',selectforeground='white')
        """
        上面这段放在这个函数里，因为这个函数是双击的时候被触发的，所以当双击的时候，选择项的前后景颜色才变化
        """
        self.cwd.set(self.dirlistbox.selection_get())
        """
        listbox和stringvar之间的信息传递
        """
        self.doLs()
    count = 0
    def doLs(self,ev = None):
        """
        到达这一步都是根据stringvar变量self.cwd里面所保存的变量来的，
        前面做的所有的功课都是改变stringvar变量，来改变路径，不管是entry框输入或者是listbox里面的选择
        """
        self.__class__.count+=1
        print 'pass..%d'%self.__class__.count
        cur = self.cwd.get()
        print cur
        error = False
        if not cur:
            cur = os.curdir
        """
        清空的时候，self.cwd里面是'',这时候点list按钮的时候空的话，会报错，所以要设置一个值。
        """

        # pdb.set_trace()

        if not os.path.exists(cur):
            # self.cwd.set('%s is not a valid path'%cur)
            # sleep(2)
            error_msg = '%s is not a valid path'%cur
            error = True
        elif not os.path.isdir(cur):
            # self.cwd.set('%s is not a dir'%cur)
            # sleep(2)
            error_msg = '%s is not a dir'%cur
            error = True
        """
        为什么输入'/U'的时候，显示的是下面那个错误，不是应该是valid path的么？？
        为什么我调试过后又自动好了？？？？？？？？？？什么情况！！！？？？
        """

        """
        上面出错的时候要处理啊，不处理直接接下去做下面的事情，上面的不就没用用了，self.cwd.set()，下面也有
        self.cwd.set()。。。。写在if error 语句之前
        """
        if error:
            # error 处理
            self.cwd.set(error_msg)
            self.top.update()
            """
            说一下这个update，如果没有这一句。文本框里面不能立刻显示出self.cwd.set的内容
            因为文本框和这个stringvar是绑定的，但是stringvar变量变动，文本框是不会立刻更新的，会在进入mainloop时更新
            这是我猜的。要想马上显示出来，就得update()一下。
            """
            sleep(2)
            if not (hasattr(self,'last') and self.last):
                print 'no self.last'
                self.last = os.curdir
            # print self.last
            self.cwd.set(self.last) # 给下一个mainloop做准备,下一次直接点击按钮list的时候会显示self.last这个目录
            """
            说一下为什么这里显示出来的一直都会是'.'即当前目录的字符
            因为在每一次成功的doLs()函数执行后，self.cwd.set(os.curdir)执行，代码后面看
            当在listbox中选择的时候，这时候执行self.last=self.cwd.get()的话，其实就是get到os.curdir。也就是'.'
            原以为会显示之前的路径名，之前的路径名保存在本段函数的cur变量里了，然后self.cwd被重新设置了。
            逻辑上，因为一开始会显示的原因，在if initdir的代码中做的是self.doLs()，
            其实这就暗示了doLs()是selectAndGo()前序.
            """
            self.dirlistbox.config(selectbackground='LightSkyBlue')
            
            self.top.update()
            return

        self.cwd.set('Fetching....')
        self.top.update()
        sleep(2)
        os.chdir(cur)
        """
        这一步我理解的是，如果你要在这个目录下做些什么，要进去这个目录
        如果不做什么，单纯只是显示目录的话这一步也是没什么的，后面的参数直接按照seld.cwd里来不用os.getcwd就可以了
        update:
        上面的不行。因为有'.','..'，这两个在，当cur保存的是'..'，的话，因为是相对的，如果要后退再后退就不行了。
        """
        self.cwd.set(os.curdir)
        self.dirlabel.config(text=os.getcwd()) 
        # dirfiles = os.listdir(os.getcwd())
        dirfiles=os.listdir(cur)
        """
        如果是os.listdir(cur)当cur保存的是'..'时，因为前面os.chdir(cur)，已经后退了一次，而在这个目录下显示'..',
        相当于显示的是当前的父目录，跳了两次了，应该显示当前的目录
        """
        dirfiles.sort()
        #sorted(dirfiles)不会改变原来的，会创建一个新的副本
        self.dirlistbox.delete(0,END)
        #但是我不知道END这个应该是类似宏定义的东西把，但是它的值是什么？？？
        self.dirlistbox.insert(END,os.curdir)
        self.dirlistbox.insert(END,os.pardir)

        for eachfile in dirfiles:
            self.dirlistbox.insert(END,eachfile)


        

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
