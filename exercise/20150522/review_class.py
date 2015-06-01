#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: review_class.py
# Created Time: Fri May 22 09:15:44 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def show(self):
        print "name : %s\nScore:%s"%(self.__name,self.__score);

    @property
    def get_score(self):
        return self.__score
    @get_score.setter
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("Score must be an integer");

        if value < 0 or value > 100:
            raise ValueError("Score must be between 0 ~ 100");
        self.__score = value


if __name__ == "__main__":
    stu = Student("Crayon",77);
    stu.show()
    print stu.get_score
    stu.set_score = 99
    stu.show()
