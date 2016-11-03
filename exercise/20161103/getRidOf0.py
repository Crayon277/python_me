#!/usr/bin/python
#-*- coding: utf-8 -*-

def get_rid_of_number(item):
    item_list = item.strip().split(',')
    keywords_list=[]
    for test in item_list.pop().split():
        try:
            i=float(test)
        except:
            keywords_list.append(test)
        else:
            pass
    item_list.append(' '.join(keywords_list))
    return ','.join(item_list)+'\n'

with open('TRAIN.csv') as fin, open('TRAIN_2.csv','w') as fw:
    fw.write(fin.readline())
    for item in fin:
        if not '0' in item.split(',')[1:4]:
            fw.write(get_rid_of_number(item))
    #f=fin.readline()
    #print get_rid_of_number(f)
