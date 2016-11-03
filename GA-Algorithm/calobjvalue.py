import math

def decodechrom(pop): #将种群的二进制基因转化为十进制（0,1023）
    temp = [];
    for i in range(len(pop)):
        t = 0;
        for j in range(10):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp

def calobjvalue(pop): #计算目标函数值
    temp1 = [];
    objvalue = [];
    temp1 = decodechrom(pop)
    for i in range(len(temp1)):
        x = temp1[i] * 10 / 1023 #（0,1023）转化为 （0,10）
        objvalue.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    return objvalue #目标函数值objvalue[m] 与个体基因 pop[m] 对应 
