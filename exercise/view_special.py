#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: view_special.py
# Created Time: Sun May 17 09:55:27 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import os,sys,view_all




def search_special(file):
    with open(file,'r') as fp:
        while 1:
            line = fp.readline()
            if len(line) == 0:
                break
            if 'KeyboardInterrupt' in line:
                res.append(file)
                break
    if not (file in res):
        print "%s has no keyword 'KeyboardInterrupt'"%file

def traver_path(main_dir):
    for path_name in os.listdir(main_dir):
        if os.path.isdir(path_name):
            traver_path(os.path.join(os.path.abspath(main_dir),path_name))
        if os.path.isfile(path_name):
            if path_name[-3:] == '.py':
                search_special(os.path.join(os.path.abspath(main_dir),path_name))

def traver_dir(main_dir):
    for root,dirs,files in os.walk(main_dir):
        print root,dirs,files
        for file in files:
            if file[-3:] == '.py':
                search_special(root + '/' + file)
            

if __name__ == "__main__":
    res = []
   # traver_path('.')
   # print res
    traver_dir('.')
    for item in res:
        view_all.print_file(item)
