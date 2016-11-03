

import graphlab
from collections import Counter

noise=['613','512','623', '511', '521', '415', '616', '526', '122', '321', '425', '212', '522', '222', '325', '614', '525', '121', '211','612','515']
def pre_handle_data(data):
     #data_sframe_without_zero = data_sframe[data_sframe[target]!=0]
    data['id'] = data.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))
    data['id'] = data['id'].apply(lambda x: None if x in noise else x)
    data = data[data['id'] != None]
    print 'get rid of noise done!...'
    return data

def handle_result_query(sframe):
    #return str like '114', finally
    result_each_count = zip(*sframe['reference_label'])
    cage = Counter(result_each_count[0]).most_common(1)[0][0]
    cgender = Counter(result_each_count[1]).most_common(1)[0][0]
    ceducation = Counter(result_each_count[2]).most_common(1)[0][0]
    return cage,cgender,ceducation

keyword_train = graphlab.SFrame('TRAIN_4_tag_without_unknown.csv')
keyword_test = graphlab.SFrame('TEST_4_tag_without_unknown.csv')

keyword_train = pre_handle_data(keyword_train)

keyword_train['word_count'] = graphlab.text_analytics.count_words(keyword_train['query_list'])
keyword_test['word_count'] = graphlab.text_analytics.count_words(keyword_test['query_list'])

keyword_train['tfidf'] = graphlab.text_analytics.tf_idf(keyword_train['word_count'])
keyword_test['tfidf'] = graphlab.text_analytics.tf_idf(keyword_test['word_count'])

#keyword_train['id'] = keyword_train.apply(lambda x:str(x['age'])+str(x['gender'])+str(x['education']))

knn_model = graphlab.nearest_neighbors.create(keyword_train,features=['tfidf'],label='id')

fw = open('result_5_knn.csv','w')
for total,sequence in enumerate(keyword_test['sequence']):
    single_item = keyword_test[keyword_test['sequence'] == sequence]
    originalID=single_item['id'][0]
    #originalAge,originalGender,originalEducation = single_item['age'][0],single_item['gender'][0],single_item['education'][0]
    knn_result = knn_model.query(single_item,k=27) #7 nearest_neighbors
    resultAge,resultGender,resultEducation = handle_result_query(knn_result)
    fw.write(originalID+' '+resultAge+' '+resultGender+' '+resultEducation+'\n')
fw.close()
print total
