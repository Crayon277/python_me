#!/usr/bin/python
#-*- coding: utf-8 -*-


'''
task
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20


'''

from collections import OrderedDict
od = OrderedDict()
for _ in range(int(raw_input())):
    record = raw_input().split()
    item = ' '.join(record[:-1])
    price=int(record[-1])
    od[item]=od.get(item,0)+price
for key,value in od.iteritems():
    print key,value
    #print '{} {}'.format(key,value)



#python3
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)

'''

rpartition(...)
    S.rpartition(sep) -> (head, sep, tail)

    Search for the separator sep in S, starting at the end of S, and return
    the part before it, the separator itself, and the part after it.  If the
    separator is not found, return two empty strings and S.

'''
