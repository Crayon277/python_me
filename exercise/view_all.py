#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: view_all.py
# Created Time: Sun May 17 09:34:33 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import os,sys


def print_file(file_name):
    print "=========%s==========="%file_name
    with open(file_name,'r') as fp:
        while True:
            line = fp.readline()
            if len(line) == 0:
                break
            print line
    print "=========%s end======="%file_name

def traverling(dir_path):
    for x in os.listdir('./'+dir_path):
        if x[-3:] == '.py':
            print_file('./' + dir_path + '/' + x)


if __name__ == "__main__":
    if len(sys.argv) <2:
        print "Argument miss"
        sys.exit()

    traverling(sys.argv[1])
