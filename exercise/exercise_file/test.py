#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import path
path.append(r'/usr/local/lib/python2.7/site-packages')
import chardet
response = None
#尝试下载网页
try:
    response = urllib2.urlopen("http://www.runoob.com/python/python-exercise-example64.html")
except Exception as e:
    print "错误：下载网页时遇到问题：" + str(e)
    # return

if response.code != 200:
    print "错误：访问后，返回的状态代码（Code）并不是预期值【200】，而是【" + str(response.code) + "】"
    # return

if response.msg != "OK":
    print "错误：访问后，返回的状态消息并不是预期值【OK】，而是【" + response.msg + "】"
    # return

#读取html代码
htmlCode = None
try:
    htmlCode = response.read()
except Exception as e:
    print "错误：下载完毕后，从响应流里读出网页代码时遇到问题：" + str(e)
    # return

#处理网页编码
htmlCode_encode = None
try:
    #猜编码类型
    htmlCharsetGuess = chardet.detect(htmlCode)
    htmlCharsetEncoding = htmlCharsetGuess["encoding"]
    #解码
    htmlCode_decode = htmlCode.decode(htmlCharsetEncoding)
    #获取系统编码
    currentSystemEncoding = sys.getfilesystemencoding()
    #按系统编码，再进行编码。
    '''
        做这一步的目的是，让编码出来的东西，可以在python中进行处理
        比如: 
             key = "你好"
             str = "xxxx你好yyyy"
             keyPos = str.find( key )
        如果不做再编码，这一步就可能会报错出问题
    '''
    htmlCode_encode = htmlCode_decode.encode(currentSystemEncoding)
except Exception as e:
    print "错误：在处理网页编码时遇到问题：" + str(e)
    # return
#htmlCode_encode即为所求
# return htmlCode_encode

print htmlCode_encode
