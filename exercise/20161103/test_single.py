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
def input_data(train_file,divide_number,end_number,tags):
    train_words = []
    train_tags=[]
    train_tags_age = []
    train_tags_gender= []
    train_tags_education = []
    test_words = []
    test_tags=[]
    test_tags_age = []
    test_tags_gender= []
    test_tags_education= []
    with open(train_file, 'r',encoding='gb18030') as f:
        text=f.readlines()
        train_data=text[:divide_number]   
        for single_query in train_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)#id
            if(single_query_list[tags]!='0'):
                train_tags.append(single_query_list[tags])
                single_query_list.pop(0)
                single_query_list.pop(0)
                single_query_list.pop(0)
                train_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
           # print(train_words)
        #print(train_tags_gender)
        test_data=text[divide_number:end_number]   
        for single_query in test_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)#id
            if(single_query_list[tags]!='0'):
                test_tags.append(single_query_list[tags])
                single_query_list.pop(0)
                single_query_list.pop(0)
                single_query_list.pop(0)
                test_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
       # print(test_words)
        #print(test_tags_age)
    print('input_data done!')
    return train_words, train_tags, test_words, test_tags

 
def input_data_write_tags(train_file, test_file,tags):
    train_words = []
    train_tags=[]
    train_tags_age = []
    train_tags_gender= []
    train_tags_education = []
    test_words = []
    test_tags_age = []
    test_tags_gender= []
    test_tags_education= []
   # with open(train_file, 'r') as train_data:
    with open(train_file, 'r',encoding='gb18030') as f:
        text=f.readlines()
        train_data=text[0:]   
        for single_query in train_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)#id
            #if(single_query_list[tags]!='0'):
            train_tags.append(single_query_list[tags])
            single_query_list.pop(0)
            single_query_list.pop(0)
            single_query_list.pop(0)
            train_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
           # print(train_words)
        #print(train_tags)
    with open(test_file, 'r') as f:
        text=f.readlines()
        test_data=text[0:]
        for single_query in test_data:
            single_query_list = single_query.split(' ')
            single_query_list.pop(0)
            test_words.append((str(single_query_list)).replace(',',' ').replace('\'','').lstrip('[').rstrip(']').replace('\\n',''))
            
   
    print('input_data done!')
    return train_words, train_tags,test_words

 
def write_test_tags(test_file,test_tags_age,test_tags_gender,test_tags_education):
    pass
    test_ID=[]
    with open(test_file,'r') as test_data:
        for single_query in test_data:
            single_query_list=single_query.split(' ')
            test_ID.append(single_query_list[0])

    with open('test_tags_file.csv','w',encoding='gbk') as test_tags_file:
        for x in range(0,len(test_tags_age)):
            test_tags_file.write(test_ID[x]+' '+test_tags_age[x]+' '+test_tags_gender[x]+' '+test_tags_education[x]+'\n')  
  
def vectorize(train_words,test_words,n_feature):
    print ('*************************\nHashingVectorizer\n*************************')  
    v = HashingVectorizer(n_features=n_feature,non_negative =True)
    print("n_features:%d"%n_feature)
    train_data = v.fit_transform(train_words)
    test_data = v.fit_transform(test_words)
    print ("the shape of train is "+repr(train_data.shape))
    print ("the shape of test is "+repr(test_data.shape)) 
    
     
    return train_data, test_data
    #print('vectorize done!')
    
    
    

def tfidf_vectorize(train_words,test_words):
    #method 2:TfidfVectorizer  
    print ('*************************\nTfidfVectorizer\n*************************')  
    from sklearn.feature_extraction.text import TfidfVectorizer  
    tv = TfidfVectorizer(sublinear_tf = True,  max_df = 0.5) # 
                                          
    tfidf_train_2 = tv.fit_transform(train_words);  #得到矩阵
    tv2 = TfidfVectorizer(vocabulary = tv.vocabulary_);  
    tfidf_test_2 = tv2.fit_transform(test_words);  
    print ("the shape of train is "+repr(tfidf_train_2.shape))  
    print ("the shape of test is "+repr(tfidf_test_2.shape))
    analyze = tv.build_analyzer()  
    tv.get_feature_names()#statistical features/terms 
    return  tfidf_train_2 ,tfidf_test_2

def SVM_single(train_data,test_data,train_tags): 
#SVM Classifier  
    from sklearn.svm import SVC  
    print ('*************************\nSVM\n*************************' )
    svclf = SVC(kernel = 'linear')#default with 'rbf'  
    svclf.fit(train_data,train_tags)  
    pred_tags = svclf.predict(test_data) 
    #print(pred_tags_gender) 
    #print(train_tags_gender)
    print('clf done!')
    return pred_tags
def evaluate_single(test_tags, test_tags_pre):
    actual=test_tags
    pred=test_tags_pre
    print ('precision:{0:.3f}'.format(sklearn.metrics.accuracy_score(actual, pred)))

def feature_selection_chi2(train_data,train_tags,test_data,n_dimensionality):
    from sklearn.feature_selection import SelectKBest, chi2
    print('feature_selection_chi2'+'\n'+'n_dimensionality:%d' %n_dimensionality)
    ch2= SelectKBest(chi2, k=n_dimensionality)
    train_data=ch2.fit_transform(train_data,train_tags)
    test_data=ch2.transform(test_data)
    #return clf.feature_importances_ 
    return train_data  , test_data         
def test():

    #train_file = 'TRAIN_4_tag_without_unknown.txt'
    #train_file = 'train_data_fenci.txt'
    train_file = 'TRAIN_4_tag_without_unknown.txt'
    print('file:'+train_file)
    devide_number=1500
    end_number=1762#17633
    n_feature=100000
    tags=0
    print('tags:%d' %tags )
    #将数据分为训练与测试，获取训练与测试数据的标签
    train_words, train_tags,test_words, test_tags = input_data(train_file,devide_number,end_number,tags)
    #向量化
    #train_data,test_data = vectorize(train_words,test_words,n_feature)
    train_data,test_data = tfidf_vectorize(train_words,test_words)
    
    # 预测
    test_tags_pre=SVM_single(train_data,test_data,train_tags)
    #计算正确率
    evaluate_single(numpy.asarray(test_tags), test_tags_pre)
def test():
    
    #test_single(0,100000)
    test_single(1,10000)
    #test_single(2,100000)
def test_single(tags,n_dimensionality):
    #train_file = 'TRAIN_4_tag_with_unknown.txt'
    train_file = 'train_data_fenci.txt'
    devide_number=15000
    end_number=17633#17633
    n_feature=100000
    print('file:'+train_file)
    print('tags:%d   ' %tags )
    #将数据分为训练与测试，获取训练与测试数据的标签
    train_words, train_tags,test_words, test_tags = input_data(train_file,devide_number,end_number,tags)
    #向量化
    #train_data,test_data = vectorize(train_words,test_words,n_feature)
    train_data,test_data = tfidf_vectorize(train_words,test_words)
     #特征提取
    train_data,test_data=feature_selection_chi2(train_data,train_tags,test_data,n_dimensionality)
    # 预测
    test_tags_pre=SVM_single(train_data,test_data,train_tags)
    #计算正确率
    evaluate_single(numpy.asarray(test_tags), test_tags_pre)


def write_single(train_file,test_file,tags,n_dimensionality):
    
    train_words, train_tags, test_words = input_data_write_tags(train_file, test_file,tags)
    #向量化
    train_data,test_data = tfidf_vectorize(train_words,test_words)
    #特征提取
    train_data,test_data=feature_selection_chi2(train_data,train_tags,test_data,n_dimensionality)
    #预测
    test_tags_pre=SVM_single(train_data,test_data,train_tags)
    return test_tags_pre
def write():
    train_file='train_data_fenci.txt'
    test_file = 'test_data_fenci.txt'
    test_tags_age_pre=write_single(train_file,test_file,0,100000)
    test_tags_gender_pre=write_single(train_file,test_file,1,10000)
    test_tags_education_pre=write_single(train_file,test_file,2,100000)
    write_test_tags(test_file,test_tags_age_pre,test_tags_gender_pre,test_tags_education_pre)

def main():
    # if len(sys.argv) < 2:
    #     print ('[Usage]: python classifier.py train_file test_file')
    #     sys.exit(0)
    # if(sys.argv[1]=="test"):
    #     test()
    # if(sys.argv[1]=="write"):
   # write()
    test()
if __name__ == '__main__':
    main()




