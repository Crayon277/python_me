def best(pop, fitvalue): #找出适应函数值中最大值，和对应的个体
	px = len(pop)
	bestindividual = []
	bestfit = fitvalue[0]
	for i in range(1,px):
		if(fitvalue[i] > bestfit):
			bestfit = fitvalue[i]
			bestindividual = pop[i]
	return [bestindividual, bestfit]
