# s= raw_input()
# index,c = input(),raw_input()
# l = list(s)
# l[index] = c
# print ''.join(l)

string=raw_input()
k=raw_input()
j=k.split(" ")
string=string[:int(j[0])]+j[1]+string[int(j[0])+1:]
print string
