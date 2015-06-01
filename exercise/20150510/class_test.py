#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: class.py
# Created Time: Sun May 10 17:31:27 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def show(self):
        print "Name: %s\nScore: %s"%(self.__name, self.__score)
    
    def get_score(self):
        return self.__score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("Score must be an integer!")
        if value < 0 or value >100:
            raise ValueError("Score must be between 0~100")
        self.__score = value



if __name__ == "__main__":
   # bar = Student("Crayon","77")
    #bar.show()
    stu = Student("crayon",'77')
    stu.set_score(60)
    print stu.get_score()

