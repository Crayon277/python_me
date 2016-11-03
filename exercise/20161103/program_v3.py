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

def select_character(data_sframe):
    '''
    每个纬度的不为0的选出来
    '''
    age_data = data_sframe[data_sframe['age']!=0]
    gender_data = data_sframe[data_sframe['gender']!=0]
    education_data = data_sframe[data_sframe['education']!=0]
    return age_data,gender_data,education_data

def score(a,b):
    count = 0
    for i,item in enumerate(a):
        if item==b[i]:
            count+=1
    return float(count)/len(a)

start = time.time()

mode = 1

data=graphlab.SFrame('./datasets/TRAIN_7_tfidf_stopwords_with_unknown.csv')
test_data = graphlab.SFrame('./datasets/TEST_7_tfidf_stopwords_with_unknown.csv')
# data_test = graphlab.SFrame('TEST_5_custom_without_unknown.csv')
# train_data = pre_handle_data(data)
#train_data,test_data = data.random_split(.8,seed=0)

age_sframe,gender_sframe,education_sfame=select_character(data)

age_tmp=[]
gender_tmp=[]
education_tmp=[]
SGC_clf_pipeline = Pipeline([('vect',CountVectorizer()),
                      ('tfidf',TfidfTransformer()),
                      ('select',SelectKBest(chi2,101277)),
                    #   ('clf',SGDClassifier(loss = 'hinge',penalty = 'l2',alpha = 1e-3,n_iter = 5, random_state = 42)),
                      ('clf',SVC(kernel='linear'))
                      ])

age_education_pipeline = Pipeline([('vect',TfidfVectorizer()),
                                    ('select',SelectKBest(chi2,101277)),
                                   ('clf',SVC(kernel='rbf',C=4.0,gamma=1.0))
])
gender_pipeline = Pipeline([('vect',TfidfVectorizer()),
                            ('select',SelectKBest(chi2,101277)),
                            ('clf',SVC(kernel='rbf',C=1.0,gamma=1.0))
])

for i in range(10):
    print 'doing.....',i+1
    age_train_reserve_data,age_train_kick_data = age_sframe.random_split(.8,seed=772)
    age_train_reserve_original_data,age_train_reserve_duplicate_data = age_train_reserve_data.random_split(.75,seed=277)
    age_train_reserve_data.append(age_train_reserve_duplicate_data)
    print 'age random select done'
    gender_train_reserve_data,gender_train_kick_data = gender_sframe.random_split(.8,seed=77)
    gender_train_reserve_original_data,gender_train_reserve_duplicate_data = gender_train_reserve_data.random_split(.75,seed=27)
    gender_train_reserve_data.append(gender_train_reserve_duplicate_data)
    print 'gender random select done'
    education_train_reserve_data,education_train_kick_data = education_sframe.random_split(.8,seed=127)
    education_train_reserve_original_data,education_train_reserve_duplicate_data = education_train_reserve_data.random_split(.75,seed=5277)
    education_train_reserve_data.append(education_train_reserve_duplicate_data)
    print 'education random select done'
# text_clf = Pipeline([('vect',CountVectorizer(stop_words="english",decode_error='ignore')),
#                     ('tfidf',TfidfTransformer()),
#                     ('clf',MultinomialNB()),
#                     ])



    for _ in ['age','gender','education']:
        print '\t',i+1,': ',_
        if _ == 'age':
            age_education_pipeline.fit(age_train_reserve_data['query_list'],age_train_reserve_data[_])
            pre = age_education_pipeline.predict(test_data['query_list'])
            eval(_+'_tmp.append(list(pre))')
        if _ == 'gender':
            gender_pipeline.fit(gender_train_reserve_data['query_list'],gender_train_reserve_data[_])
            pre = gender_pipeline.predict(test_data['query_list'])
            eval(_+'_tmp.append(list(pre))')
        if _ == 'education':
            age_education_pipeline.fit(education_train_reserve_data['query_list'],education_train_reserve_data[_])
            pre = age_education_pipeline.predict(test_data['query_list'])
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

with open('result_9_singel_zeros.csv','w') as fw:
    for index,item in enumerate(test_data):
        fw.write(item['id'].decode('utf-8').encode('gbk')+' '+str(age_result[index]).encode('gbk')+' '+str(gender_result[index]).encode('gbk')+' '+str(education_result[index]).encode('gbk')+'\n')
end = time.time()
print 'use time',end-start
