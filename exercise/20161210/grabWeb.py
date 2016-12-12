#!/usr/bin/env python
# coding=utf-8

'''
这个程序是利用在从互联网抓取一个web页面来证明默认参数的好处

这个联系显示从web页面上获取的第一和最后的非空行，
由于download函数的双默认参数允许用不同的urls或者制定不同的处理函数来进行覆盖，灵活性得到了提升

'''

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachline in lines:
        if not eachline.strip():  #判断是否是空行, 如果是就继续，因为我们要的不是空行
            continue
        else:
            return eachline

def firstLast(webpage):
    f = open(webpage) #这个webpage是已经下载好了的网页文件。所以用open
    lines = f.readlines()
    print firstNonBlank(lines)
    lines.reverse()#上面打印了第一个非空行，只要将这个列表反之，再调用这个函数就是最后一个非空行！！！
    print firstNonBlank(lines)
    f.close()

def download(url='http://www',process=firstLast): #将函数名作为参数
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__main__':
    download()
