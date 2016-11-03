#!/usr/bin/env python
# coding=utf-8

import graphlab
from sklearn.feature_extraction.text import TfidfVectorizer as Tfv
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from collections import Counter
import pickle
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
def score(a,b):
    count = 0
    for i,item in enumerate(a):
        if item==b[i]:
            count+=1
    return float(count)/len(a)

start = time.time()

mode = 1

data=graphlab.load_sframe('TRAIN_6_cut_without_unknown_without_noise')
test_data = graphlab.SFrame('TEST_6_cut_without_unknown.csv')
# data_test = graphlab.SFrame('TEST_5_custom_without_unknown.csv')
# train_data = pre_handle_data(data)
#train_data,test_data = data.random_split(.8,seed=0)
age_tmp=[]
gender_tmp=[]
education_tmp=[]

for i in range(10):
    print 'doing.....',i+1
    train_reserve_data,train_kick_data = data.random_split(.8,seed=772)
    train_reserve_original_data,train_reserve_duplicate_data = train_reserve_data.random_split(.75,seed=277)
    train_reserve_data.append(train_reserve_duplicate_data)

# text_clf = Pipeline([('vect',CountVectorizer(stop_words="english",decode_error='ignore')),
#                     ('tfidf',TfidfTransformer()),
#                     ('clf',MultinomialNB()),
#                     ])

    SGC_clf_pipeline = Pipeline([('vect',CountVectorizer()),
                          ('tfidf',TfidfTransformer()),
                          ('select',SelectKBest(chi2,101277)),
                        #   ('clf',SGDClassifier(loss = 'hinge',penalty = 'l2',alpha = 1e-3,n_iter = 5, random_state = 42)),
                          ('clf',SVC(kernel='linear'))
                          ])

    for _ in ['age','gender','education']:
        print '\t',i+1,': ',_
        SGC_clf_pipeline.fit(train_reserve_data['query_list'],train_reserve_data[_])
        pre = SGC_clf_pipeline.predict(test_data['query_list'])
        eval(_+'_tmp.append(list(pre))')

print 'age_len',len(age_tmp)
print 'gender_len',len(gender_tmp)
print 'education_len',len(education_tmp)
age=zip(*age_tmp)
gender=zip(*gender_tmp)
education=zip(*education_tmp)

print 'age_len',len(age)
print 'gender_len',len(gender)
print 'education_len',len(education)
age_result=[Counter(item).most_common(1)[0][0] for item in age]
gender_result=[Counter(item).most_common(1)[0][0] for item in gender]
education_result=[Counter(item).most_common(1)[0][0] for item in education]

print 'age_len',len(age_result)
print 'gender_len',len(gender_result)
print 'education_len',len(education_result)

with open('age.pickle','wb') as fage:
    pickle.dump(age_result,fage)
with open('gender.pickle','wb') as fgender:
    pickle.dump(gender_result,fgender)
with open('education.pickle','wb') as feducation:
    pickle.dump(education_result,feducation)


#
# for _ in ['age','gender','education']:
#     # forlist=list(test_data[_])
#     tmp = eval('score('+_+'_result,test_data[_])')
#     print tmp

with open('result_8_combination_10times.csv','w') as fw:
    for index,item in enumerate(test_data):
        fw.write(item['id'].decode('utf-8').encode('gbk')+' '+str(age_result[index]).encode('gbk')+' '+str(gender_result[index]).encode('gbk')+' '+str(education_result[index]).encode('gbk')+'\n')
end = time.time()
print 'use time',end-start
