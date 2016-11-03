

import graphlab
from collections import Counter

def handle_result_query(sframe):
    #return str like '114', finally
    result_each_count = zip(*sframe['reference_label'])
    cage = Counter(result_each_count[0]).most_common(1)[0][0]
    cgender = Counter(result_each_count[1]).most_common(1)[0][0]
    ceducation = Counter(result_each_count[2]).most_common(1)[0][0]
    return cage,cgender,ceducation

keyword_train = graphlab.SFrame('TRAIN_3_textrank.csv')

keyword_train['word_count'] = graphlab.text_analytics.count_words(keyword_train['query_list'])

keyword_train['tfidf'] = graphlab.text_analytics.tf_idf(keyword_train['word_count'])

keyword_train['id'] = keyword_train.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))

train_data,test_data = keyword_train.random_split(.8,seed=0)

knn_model = graphlab.nearest_neighbors.create(train_data,features=['tfidf'],label='id')

count_age=0
count_gender=0
count_education=0

#fw = open('result.csv','w')
for total,sequence in enumerate(test_data['sequence']):
    single_item = test_data[test_data['sequence'] == sequence]
    #originalID=single_item['id'][0]
    originalAge,originalGender,originalEducation = single_item['age'][0],single_item['gender'][0],single_item['education'][0]
    knn_result = knn_model.query(single_item,k=17) #7 nearest_neighbors
    resultAge,resultGender,resultEducation = handle_result_query(knn_result)
    #fw.write(originalID+' '+resultAge+' '+resultGender+' '+resultEducation+'\n')
    if str(resultAge) == str(originalAge):
        count_age += 1
    if str(resultGender) == str(originalGender):
        count_gender += 1
    if str(resultEducation) == str(originalEducation):
        count_education+=1

print 'age {}'.format(float(count_age)/total)
print 'gender {}'.format(float(count_gender)/total)
print 'education {}'.format(float(count_education)/total)

print count_age,count_gender,count_education,total
