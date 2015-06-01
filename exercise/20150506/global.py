def func(a):
        global x
        a += 1
        print "parameter named a ",a
        
        print "In function",x
        x = x + 1

x = 2
print "Outside",x
func(x)
print "After function",x
