#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: kelly.py
# Created Time: Wed Sep  7 08:02:22 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import sanitize

julie = []
james = []
sarah = []
mikey = []

with open('julie.txt','r') as julie_file,open('james.txt','r') as james_file, open('sarah.txt','r') as sarah_file, open('mikey.txt','r') as mikey_file:
    julie_data = julie_file.readline()
    julie = julie_data.strip().split(',')
    james_data = james_file.readline()
    james = james_data.strip().split(',')
    sarah_data = sarah_file.readline()
    sarah = sarah_data.strip().split(',')
    mikey_data = mikey_file.readline()
    mikey = mikey_data.strip().split(',')

print julie
print james
print sarah
print mikey

print '======================='
clean_julie = [sanitize.sanitize_2(item) for item in julie]
clean_james = [sanitize.sanitize_2(item) for item in james]
clean_sarah = [sanitize.sanitize_2(item) for item in sarah]
clean_mikey = [sanitize.sanitize_2(item) for item in mikey]

print sorted(clean_julie)
print sorted(clean_james)
print sorted(clean_sarah)
print sorted(clean_mikey)

sorted_julie=sorted(clean_julie)
sorted_james=sorted(clean_james)
sorted_sarah=sorted(clean_sarah)
sorted_mikey=sorted(clean_mikey)


print '======================='
#需要删除重复项
# for i in clean_julie:
    # chongfu = clean_julie.count(i)
    # if chongfu > 1:
        # start = clean_julie.index(i)+1
        # for cnt in range(chongfu-1):
            # clean_julie.remove(clean_julie[cnt])
            # print clean_julie
    # else:
        # pass

# print clean_julie
#上面的这种方法很复杂，而且结果是错的。
#我的思维往往都是就地的，c语言式的，相对这个列表做什么
#重新创建一个新列表

unique_julie = []
for item in sorted_julie:
    if item not in unique_julie:
        unique_julie.append(item)
    else:
        pass
print unique_julie

#现有列表中删除重复项，集合！！

set_julie = set(sorted_julie) #但是最后是无序的集合
print set_julie

print '======================='

print sorted(set(clean_julie))[0:3]

