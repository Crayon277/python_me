
N, M = map(int,raw_input().split())
#主要是这个输入的，map返回的是一个list，如果只有一个变量接受，那那个变量就是指向一个list，
#如果好几个，那就是unpack赋值，此时list当中元素的个数要和变量个数是一致的！
for i in xrange(1,N,2):
    print ('.|.'*i).center(3*N,'-')
print 'WELCOME'.center(3*N,'-')
for i in xrange(N-2,-1,-2): #还有这个，range的范围到－1为止截止，不要和切片里面的－1混淆，好老是想怎么到最后一个元素去了，这里是一个概念么？！！
    print ('.|.'*i).center(3*N,'-')
