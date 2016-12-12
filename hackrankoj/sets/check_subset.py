for i in range(int(raw_input())):
    a = int(raw_input()); A = set(raw_input().split());
    b = int(raw_input()); B = set(raw_input().split());
    print A <= B
    #print A.issubset(B)


'''
print not bool(A.difference(B))

相当于 A-B(A中有的B没有的),如果A在B里面，那么A－B是空，bool是假，再not为真
反之，如果有，那么bool()为真，not 为假
'''

'''
还有就是A&B ＝＝ A

'''
