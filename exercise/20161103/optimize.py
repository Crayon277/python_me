#!/usr/bin/env python
# coding=utf-8

import graphlab
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
import time
#noise=['613','512','623', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211','612','515'] #<9
noise = ['613', '623', '511', '521', '415', '616', '526', '122', '425', '212', '522', '222', '525', '121', '211', '612', '515'] # < 6
#['613', '326', '512', '623', '316', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211', '612', '515']
#frequency less than 10
def pre_handle_data(data):
     #data_sframe_without_zero = data_sframe[data_sframe[target]!=0]
    data['combination'] = data.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))
    data['combination'] = data['combination'].apply(lambda x: None if x in noise else x)
    data = data[data['combination'] != None]
    print 'get rid of noise done!...'
    return data
start = time.time()
data = graphlab.load_sframe('TRAIN_6_cut_without_unknown_without_noise')
data = pre_handle_data(data)

v = TfidfVectorizer()
vec = v.fit_transform(data['query_list'])

# SGC_clf_pipeline = Pipeline([('vect',CountVectorizer()),
#                       ('tfidf',TfidfTransformer()),
#                       #('clf',SGDClassifier(loss = 'hinge',penalty = 'l2',alpha = 1e-3,n_iter = 5, random_state = 42)),
#                       ('clf',SVC())
#                       ])

C_range = np.logspace(-1, 2,4,base=2)
gamma_range = np.logspace(-1, 2,4,base=2)
param_grid = dict(gamma=gamma_range, C=C_range)
#cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
grid = GridSearchCV(SVC(), param_grid=param_grid)
fw = open('optimize_params.log','w')
for _ in ['education','age','gender']:
    print 'doing ...',_
    l=list(data[_])
    grid.fit(vec, l)
    fw.write('best_estimator: '+str(grid.best_estimator_)+'\n'+'best_params: '+str(grid.best_params_)+'\n'+'best_score: '+str(grid.best_score_)+'\n' + 'convert_result: '+str(grid.cv_results_)+'\n')
    print("The best parameters are %s with a score of %0.2f"% (grid.best_params_, grid.best_score_))
fw.close()
end = time.time()
print 'use time',end-time
