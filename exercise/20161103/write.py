# coding: utf-8

import sys
import jieba
import numpy
import sklearn
from sklearn import metrics
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import numpy as np
from sklearn.metrics import accuracy_score

def input_data(train_file,divide_number):
    train_words = []
    train_tags_age = []
    train_tags_gender= []
    train_tags_education = []
    test_words = []
    test_tags_age = []
    test_tags_gender= []
    test_tags_education= []
    with open(train_file, 'r',encoding='gb18030') as f:
        text=f.readlines()
        train_data=text[:divide_number]   #lines包括当前要处理的10行
           #text包括剩余的文本
        for single_query in train_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)#id
            train_tags_age.append(single_query_list.pop(0))
            train_tags_gender.append(single_query_list.pop(0))
            train_tags_education.append(single_query_list.pop(0))
            train_words.append(·(str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
           # print(train_words)
        #print(train_tags_gender)
        test_data=text[divide_number:]   #lines包括当前要处理的10行
           #text包括剩余的文本
        for single_query in test_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)#id
            test_tags_age.append(single_query_list.pop(0))
            test_tags_gender.append(single_query_list.pop(0))
            test_tags_education.append(single_query_list.pop(0))
            test_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
       # print(test_words)
        #print(test_tags_age)
    print('input_data done!')
    return train_words, train_tags_age,train_tags_gender,train_tags_education, test_words, test_tags_age,test_tags_gender,test_tags_education
def input_data_write_tags(train_file, test_file):
    train_words = []
    train_tags_age = []
    train_tags_gender= []
    train_tags_education = []
    test_words = []
    test_tags_age = []
    test_tags_gender= []
    test_tags_education= []
   # with open(train_file, 'r') as train_data:
    with open(train_file, 'r') as f:
    	text = f.readlines()
    	train_data=text[0:]
    	for single_query in train_data:

            single_query_list = single_query.strip().split(' ')
            single_query_list.pop(0)#id
            # if(single_query_list[0]!='0' and single_query_list[1]!='0' and single_query_list[2]!='0'):
            train_tags_age.append(single_query_list.pop(0))
            train_tags_gender.append(single_query_list.pop(0))
            train_tags_education.append(single_query_list.pop(0))
            #train_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\·\n',''))
            train_words.append(' '.join(single_query_list))
           # print(train_words)
        #print(train_tags_age)
    #with open(test_file, 'r') as test_data:
    with open(test_file, 'r') as f:
    	text=f.readlines()
    	test_data=text[0:]
    	for single_query in test_data:
            single_query_list = single_query.strip().split(' ')
            single_query_list.pop(0)
            # test_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
            test_words.append(' '.join(single_query_list))


       # print(test_words)
        #print(test_tags_age)

        #处理测试数据
        #print((train_tags))
        #(train_file,'r').close()
    print('input_data done!')
    return train_words, train_tags_age,train_tags_gender,train_tags_education, test_words

def write_test_tags(test_file,test_tags_age,test_tags_gender,test_tags_education):
    pass
    test_ID=[]
    with open(test_file,'r') as test_data:
        for single_query in test_data:
            single_query_list=single_query.split(' ')
            test_ID.append(single_query_list[0])

    with open('test_tags_file.csv','w',encoding='gbk') as test_tags_file:
        for x in range(len(test_tags_age)):
            test_tags_file.write(test_ID[x]+' '+test_tags_age[x]+' '+test_tags_gender[x]+' '+test_tags_education[x]+'\n')

def vectorize(train_words,test_words):
    v = HashingVectorizer(n_features=1000000)
    train_data = v.fit_transform(train_words)
   # print(train_data)
    test_data = v.fit_transform(test_words)
     #CountVectorizer
    #vectorizer = CountVectorizer(min_df=2)
    #train_data=vectorizer.fit_transform(train_words)

    print('vectorize done!')
    return train_data, test_data



def evaluate(test_tags_age, test_tags_age_pre,test_tags_gender, test_tags_gender_pre,test_tags_education, test_tags_education_pre):
    print ('age:')
    actual=test_tags_age
    pred=test_tags_age_pre
    print ('precision:{0:.3f}'.format(sklearn.metrics.accuracy_score(actual, pred)))

    print ('gender:')
    actual=test_tags_gender
    pred=test_tags_gender_pre
    print ('precision:{0:.3f}'.format(sklearn.metrics.accuracy_score(actual, pred)))

    print ('education:')
    actual=test_tags_education
    pred=test_tags_education_pre
    print ('precision:{0:.3f}'.format(sklearn.metrics.accuracy_score(actual, pred)))


def svm(train_data,train_tags,test_data,test_tags):
#SVM Classifier
    from sklearn.svm import SVC
    print ('*************************\nSVM\n*************************' )
    svclf = SVC(kernel = 'linear')#default with 'rbf'
    svclf.fit(train_data,train_tags)
    pred = svclf.predict(test_data)
    print('clf done!')
    calculate_result(test_tags,pred)
    return svclf
def SVM(train_data,test_data,train_tags_age,train_tags_gender,train_tags_education):
#SVM Classifier
    from sklearn.svm import SVC
    print ('*************************\nSVM\n*************************' )
    svclf = SVC(kernel = 'linear')#default with 'rbf'
    svclf.fit(train_data,train_tags_age)
    pred_tags_age = svclf.predict(test_data)
    svclf.fit(train_data,train_tags_gender)
    pred_tags_gender = svclf.predict(test_data)
    svclf.fit(train_data,train_tags_education)
    pred_tags_education = svclf.predict(test_data)
    #print(pred_tags_gender)
    #print(train_tags_age)
    print('clf done!')
   # calculate_result(test_tags,pred)
    return pred_tags_age,pred_tags_gender,pred_tags_education
def KNN(train_data,test_data,train_tags_age,train_tags_gender,train_tags_education):
######################################################
    #KNN Classifier
    from sklearn.neighbors import KNeighborsClassifier
    print ('*************************\nKNN\n*************************')
    knnclf = KNeighborsClassifier()#default with k=5
    knnclf.fit(train_data,train_tags_age)
    pred_tags_age = knnclf.predict(test_data)
    knnclf.fit(train_data,train_tags_gender)
    pred_tags_gender = knnclf.predict(test_data)
    knnclf.fit(train_data,train_tags_education)
    pred_tags_education = knnclf.predict(test_data)
    #calculate_result(test_tags,pred);
    return pred_tags_age,pred_tags_gender,pred_tags_education
def main(train_file,test_file):

    # train_file = 'train_data_fenci.txt'
    # test_file = 'train_data_fenci.txt'
    # #将数据分为训练与测试，获取训练与测试数据的标签
    # train_words, train_tags_age,train_tags_gender,train_tags_education, test_words, test_tags_age,test_tags_gender,test_tags_education = input_data(train_file,15000)
    # #向量化
    # train_data,test_data = vectorize(train_words,test_words)
    # # 预测
    # test_tags_age_pre,test_tags_gender_pre,test_tags_education_pre=SVM(train_data,test_data,train_tags_age,train_tags_gender,train_tags_education)
    # #计算正确率
    # evaluate(numpy.asarray(test_tags_age), test_tags_age_pre,numpy.asarray(test_tags_gender), test_tags_gender_pre,numpy.asarray(test_tags_education), test_tags_education_pre)
    #train_file = 'train_data_fenci.txt'
    #test_file = 'test_data_fenci.txt'
    train_words, train_tags_age,train_tags_gender,train_tags_education, test_words = input_data_write_tags(train_file, test_file)
    train_data,test_data = vectorize(train_words,test_words)
    test_tags_age_pre,test_tags_gender_pre,test_tags_education_pre=SVM(train_data,test_data,train_tags_age,train_tags_gender,train_tags_education)
    write_test_tags(test_file,test_tags_age_pre,test_tags_gender_pre,test_tags_education_pre)
if __name__ == '__main__':
    main('TRAIN_3_textrank_without_title.txt','TEST_3_textrank_without_title.txt')
