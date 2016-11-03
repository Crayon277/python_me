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
tfidf_age_v = Tfv(max_features = 1000000)
tfidf_gender_v = Tfv(max_features = 1000000)
tfidf_education_v = Tfv(max_features = 1000000)
tfidf_unite_v = Tfv()
hash_v = HashingVectorizer(n_features=1000000)

noise=['613','512','623', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211','612','515'] #<9
#['613', '623', '511', '521', '415', '616', '526', '122', '425', '212', '522', '222', '525', '121', '211', '612', '515'] # < 6
#['613', '326', '512', '623', '316', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211', '612', '515']
#frequency less than 10
def pre_handle_data(data):
     #data_sframe_without_zero = data_sframe[data_sframe[target]!=0]
    data['combination'] = data.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))
    data['combination'] = data['combination'].apply(lambda x: None if x in noise else x)
    data = data[data['combination'] != None]
    print 'get rid of noise done!...'
    return data

def structure_file(filename,train=1):
    print 'structure file....'
    data = graphlab.SFrame(filename)
    if train:
        return pre_handle_data(data)
    return data

def data_vector(data_sframe,mode,target=None):
    #global hash_v
    global tfidf_age_v
    global tfidf_gender_v
    global tfidf_education_v
    global tfidf_unite_v
      #set max_features = 1000000.
    #vec_all = tfidf_v.fit_transform(data_sframe['query_list'])
    print 'vectorize.....'
    if mode == 'fit':
        return eval('tfidf_'+target+"_v.fit_transform(data_sframe['query_list'])")
    elif mode == 'test':
        return eval('tfidf_'+target+"_v.transform(data_sframe['query_list'])")
    elif mode == 'unite_1':
        vv= tfidf_unite_v.fit_transform(data_sframe['query_list'])
        print vv.shape
        return vv
    else:
        return tfidf_unite_v.transform(data_sframe['query_list'])

def get_target(data_sframe,target):
    l=[]
    for item in data_sframe:
        l.append(item[target])
    print l[:10]
    return l


def select_character(data_sframe):
    '''
    每个纬度的不为0的选出来
    '''
    age_data = data_sframe[data_sframe['age']!=0]
    gender_data = data_sframe[data_sframe['gender']!=0]
    education_data = data_sframe[data_sframe['education']!=0]
    return age_data,gender_data,education_data

def all_dimension_vector(age_sframe,gender_sframe,education_sframe,mode):

    age_vec=data_vector(age_sframe,mode,'age')
    gender_vec=data_vector(gender_sframe,mode,'gender')
    education_vec=data_vector(education_sframe,mode,'education')
    return age_vec,gender_vec,education_vec

def SVM(a_kernel,train_sframe,vec_train,target):
    clf = SVC(kernel=a_kernel)
    clf.fit(vec_train,train_sframe[target])
    #clf.fit(vec_train,get_target(train_sframe,target))
    print 'SVM done !'
    return clf


def all_dimension_SVM(kernel,age_vec,age_sframe,gender_vec,gender_sframe,education_vec,education_sframe):
    print 'get all dimension SVM'
    age_clf=SVM(kernel,age_sframe,age_vec,'age')
    gender_clf = SVM(kernel,gender_sframe,gender_vec,'gender')
    education_clf = SVM(kernel,education_sframe,education_vec,'education')
    return age_clf,gender_clf,education_clf

def test_equal(a,b,c,d):
    print 'data age gender education lens are',a,b,c,d
    if not (a==b and a==c and a == d):
        raise ValueError('data length not equal')
    return None

def score(clf,vec,a):
    pre = clf.predict(vec)
    if len(pre) != len(a):
        raise ValueError('predict length may be wrong')
    a_without_zero = [i for i in a if i != 0]

    return float(sum([1 if (a[i] != 0) and (a[i] == j)  else 0 for i,j in enumerate(pre)]))/len(a_without_zero)

def classify(train_data,unno):
    if unno == 1:
        age_sframe,gender_sframe,education_sframe = select_character(train_data)
        age_vec,gender_vec,education_vec = all_dimension_vector(age_sframe,gender_sframe,education_sframe,mode='fit')
    else:
        vec = data_vector(train_data,'unite_1')
        age_sframe=gender_sframe=education_sframe=train_data
        age_vec=gender_vec=education_vec=vec

    return all_dimension_SVM('linear',age_vec,age_sframe,gender_vec,gender_sframe,education_vec,education_sframe)

def main(train_data,test_data,mode=1,unno=0):
    # train_data = structure_file(train_filename)
    # test_data = structure_file(test_filename)
    info = 'file without unkown and is TRAIN_6_cut_without_unknown\n' \
    'get rid of noise\n'\
    'using TFifdVectorizer max_features = 1000000\n'\
    'svm using linear\n'

    age_clf,gender_clf,education_clf = classify(train_data,unno=0)
    # unno = 1 is with unknoun
    # unno = 0 is wihtout unknown

    if mode == 1:#formal
        test_vec = data_vector(test_data,mode = 'unite_2')

        age_pre = age_clf.predict(test_vec)
        gender_pre = gender_clf.predict(test_vec)
        education_pre = education_clf.predict(test_vec)

        test_equal(len(test_data),len(age_pre),len(gender_pre),len(education_pre))

        with open('result_7_cut.csv','w') as fw:
            for i,item in enumerate(test_data):
                fw.write(item['id'].encode('gbk')+' '+str(age_pre[i]).encode('gbk')+' '+str(gender_pre[i]).encode('gbk')+' '+str(education_pre[i]).encode('gbk')+'\n')
    else:
        #test_age_sframe,test_gender_sframe,test_education_sframe = select_character(test_data)
        if unno == 1:
            test_age_vec,test_gender_vec,test_education_vec = all_dimension_vector(test_data,test_data,test_data,mode='test')
        else:
            test_vec = data_vector(test_data,mode = 'unite_2')
            test_age_vec=test_gender_vec=test_education_vec=test_vec

        print score(age_clf,test_age_vec,test_data['age'])
        print score(gender_clf,test_gender_vec,test_data['gender'])
        print score(education_clf,test_education_vec,test_data['education'])
        print info

if __name__ == '__main__':

    train_data = structure_file('TRAIN_6_cut_without_unknown.csv',train = 1)
    test_data = structure_file('TEST_6_cut_without_unknown.csv',train = 0)
    main(train_data,test_data,mode=1)
