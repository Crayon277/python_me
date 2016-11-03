#!/usr/bin/env python
# coding=utf-8

import graphlab
import sys
noise=['613','512','623', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211','612','515']
#<9
#noise = ['613', '623', '511', '521', '415', '616', '526', '122', '425', '212', '522', '222', '525', '121', '211', '612', '515']
# < 6
#noise = ['613', '623', '511', '415', '616', '526', '122', '522', '222', '525', '121', '211', '612', '515']
# <4
#noise = ['613', '426', '326', '512', '421', '416', '216', '624', '315', '623', '316', '226', '511', '521', '415', '616', '411', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211', '612', '515']
def pre_handle_data(data):
     #data_sframe_without_zero = data_sframe[data_sframe[target]!=0]
    data['combination'] = data.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))
    data['combination'] = data['combination'].apply(lambda x: None if x in noise else x)
    data = data[data['combination'] != None]
    print 'get rid of noise done!...'
    return data

train_data = graphlab.SFrame(sys.argv[1])
data = pre_handle_data(train_data)
data.save(sys.argv[1].replace('.csv','_without_noise'))
