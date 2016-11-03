#!/usr/bin/env python
# coding=utf-8

import graphlab
from sklearn.feature_extraction.text import TfidfVectorizer as Tfv
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import numpy as np
import time
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

start = time.time()

data = graphlab.SFrame('TRAIN_5_custom_without_unknown.csv')
data_test = graphlab.SFrame('TEST_5_custom_without_unknown.csv')
train_data = pre_handle_data(data)

# text_clf = Pipeline([('vect',CountVectorizer(stop_words="english",decode_error='ignore')),
#                     ('tfidf',TfidfTransformer()),
#                     ('clf',MultinomialNB()),
#                     ])

SGC_clf_pipeline = Pipeline([('vect',CountVectorizer()),
                      ('tfidf',TfidfTransformer()),
                      #('clf',SGDClassifier(loss = 'hinge',penalty = 'l2',alpha = 1e-3,n_iter = 5, random_state = 42)),
                      ('clf',SVC(kernel='linear'))
                      ])

result = []
for _ in ['age','gender','education']:
    SGC_clf_pipeline.fit(train_data['query_list'],train_data[_])
    pre = SGC_clf_pipeline.predict(data_test['query_list'])
    result.append(list(pre))

with open('result_5_cutstom_without_noise.csv','w') as fw:
    for index,result_tuple in enumerate(zip(*result)):
        fw.write(data_test[index]['id'].decode('utf-8').encode('gbk')+' '+str(result_tuple[0]).encode('gbk')+' '+str(result_tuple[1]).encode('gbk')+' '+str(result_tuple[2]).encode('gbk')+'\n')
end = time.time()
print 'use time',end-start
