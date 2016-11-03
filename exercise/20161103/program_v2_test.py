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



start = time.time()
#test module
#data = graphlab.SFrame('TRAIN_6_cut_without_unknown')
data=graphlab.load_sframe('TRAIN_6_cut_without_unknown_without_noise')
train_data,test_data=data.random_split(.8,seed=0)
# train_data = pre_handle_data(train_data)


# text_clf = Pipeline([('vect',CountVectorizer(stop_words="english",decode_error='ignore')),
#                     ('tfidf',TfidfTransformer()),
#                     ('clf',MultinomialNB()),
#                     ])


SGC_clf_pipeline = Pipeline([('vect',CountVectorizer()),
                      ('tfidf',TfidfTransformer()),
                      ('clf',SGDClassifier(loss = 'hinge',penalty = 'l2',alpha = 1e-3,n_iter = 5, random_state = 42)),
                    #   ('clf',SVC(kernel='linear',C=1.2))
                      ])

#test
for _ in ['age','gender','education']:
    SGC_clf_pipeline.fit(train_data['query_list'],train_data[_])
    pre = SGC_clf_pipeline.predict(test_data['query_list'])
    print np.mean(pre == test_data[_])

end = time.time()
print 'use time',end-start
