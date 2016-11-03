def calfitvalue(objvalue):#转化为适应值，目标函数值越大越好，负值淘汰。
    fitvalue = []
    temp = 0.0
    Cmin = 0;
    for i in range(len(objvalue)):
        if(objvalue[i] + Cmin > 0):
            temp = Cmin + objvalue[i]
        else:
            temp = 0.0
        fitvalue.append(temp)
    return fitvalue
