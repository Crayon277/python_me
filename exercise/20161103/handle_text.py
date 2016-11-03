#!/usr/bin/python
#-*- coding: utf-8 -*-

# import sys
# sys.path.append('C:\\program files\\anaconda3\\lib\\site-packages')
import jieba.analyse
#import list_encoding
import math
math_query = dir(math)
math_query.extend(['lim','^','+','-','*','/','='])

allowpos = ('an', 'i', 'j', 'l', 'n', 'ns', 'nt', 'nx', 'nz', 's', 'v', 'vn')

keywords_total_number = 0
prefix_train ='id,age,gender,education,query_list'
prefix_test = 'id,query_list'



# stop_words_file = open('stopwords.txt')
# stopwords_list = [item.strip().decode('gb18030') for item in stop_words_file]
# stopwords_list.extend(['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'])
def extract_keyword_tags(sentence,keywords_list):
    jieba.analyse.set_stop_words('stopwords_utf_8.txt')
    keywords_list = jieba.analyse.extract_tags(sentence)#,allowPOS=allowpos)

    return keywords_list

def extract_keyword_textrank(sentence,keywords_list):
    tmp_list = jieba.analyse.textrank(sentence)#,allowPOS=allowpos)
    for item in tmp_list:
        try:
            i=float(item)
        except:
            keywords_list.append(item)
        else:
            pass
    return keywords_list

def extract_custom(sentence,keywords_list):
    global stopwords_list
    # keywords_list.extend([i for i in jieba.cut_for_search if i not in stopwords_list])
    for item in jieba.cut(sentence):
        try:
            i = float(item)
        except:
            if item not in stopwords_list:
                keywords_list.append(item)
        else:
            pass

def deal_with_special(sentence,keywords_list): #
    #ignore url,公式
    pass

def handle_singel_item(query,drop,enc='gb18030',mode=3): #Train: mode = 3, drop=1; TEST: mode=1,drop=0
    global keywords_total_number
    keywords_list=[]
    query_decode_list = query.decode(enc).split()[drop:]
    #print str(list_encoding.list_encode(query_decode_list)).decode('string_escape')

    '''
    未知的踢掉
    '''
    # if mode == 3 and '0' in query_decode_list[:3]:
    #     return False

    for item in query_decode_list[mode:]:
        if 'http' in item or any([1 if match in item else 0 for match in math_query]):
            deal_with_special(item,keywords_list)
        else:
            extract_keyword_tags(item,keywords_list)
            #extract_keyword_textrank(item,keywords_list)
            #extract_custom(item,keywords_list)

    keywords_str = ' '.join(keywords_list)
    keywords_total_number+=len(keywords_list)
    return ','.join(query_decode_list[:mode]+[keywords_str])

def extract_file_and_write_file(filename,wfile,drop,enc,mode):
    try:
        with open(filename) as fin:
            print 'open ...',fin.name

            #return iter(reduce(lambda x,y:x+y,[jieba.analyse.textrank(sentence) for query in fin for sentence in query.decode(enc).split()[drop:]]))
            try:
                with open(wfile,'w') as fw:
                    if mode == 3:
                        fw.write(prefix_train+'\n')
                    else:
                        fw.write(prefix_test+'\n')
                    for i,query in enumerate(fin):
                        to_be_written = handle_singel_item(query,drop,enc,mode) #得到 1 1 4 ${关键词字符串以空格隔开}
                        if to_be_written:
                            fw.write(str(i+1)+','+to_be_written.encode('utf-8')+'\n') #得到一个写入一个
                        print '{:2.2f}%\x08\x08\x08\x08\x08\x08\x08'.format(float(i+1)/200),
            except IOError as ee:
                print 'wfile error',e

    except IOError as e:
        print 'file error',e




if __name__ == '__main__':

    extract_file_and_write_file('user_tag_query.2W.TRAIN','./datasets/TRAIN_7_tfidf_stopwords_with_unknown.csv',1,'gb18030',3)
    print 'keywords_total_number in TRAIN',keywords_total_number
    keywords_total_number = 0
    extract_file_and_write_file('user_tag_query.2W.TEST','./datasets/TEST_7_tfidf_stopwords_with_unknown.csv',0,'gb18030',1)
    print 'keywords_total_number in TEST',keywords_total_number
