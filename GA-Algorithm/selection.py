import random

def sum(fitvalue):
    total = 0
    for i in range(len(fitvalue)):
        total += fitvalue[i]
    return total

def cumsum(fitvalue):
    for i in range(len(fitvalue)):
        t = 0;
        j = 0;
        while(j <= i):
            t += fitvalue[j]
            j = j + 1
        fitvalue[i] = t;

def selection(pop, fitvalue): #自然选择（轮盘赌算法）
	newfitvalue = []
	totalfit = sum(fitvalue)
	for i in range(len(fitvalue)):
		newfitvalue.append(fitvalue[i] / totalfit)
	cumsum(newfitvalue)
	ms = [];
	poplen = len(pop)
	for i in range(poplen):
		ms.append(random.random()) #random float list ms
	ms.sort()
	fitin = 0
	newin = 0
	newpop = pop
	while newin < poplen:
		if(ms[newin] < newfitvalue[fitin]):
			newpop[newin] = pop[fitin]
			newin = newin + 1
		else:
			fitin = fitin + 1
	pop = newpop
