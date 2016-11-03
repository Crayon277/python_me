#!/usr/bin/env python
# coding=utf-8
# import io
def convert_result():
    with open('result.csv') as fin, open('final.csv','w') as fw:
        for line in fin:
            line_list = line.strip().split()
            fw.write(line_list[0][2:34].decode('utf-8').encode('gbk')+' '+line_list[1].decode('utf-8').encode('gbk')+' '+line_list[2].decode('utf-8').encode('gbk')+' '+line_list[3].decode('utf-8').encode('gbk')+'\n')
prefix_train ='sequence,age,gender,education,query_list'
prefix_test = 'sequence,id,query_list'
def add_title(filename):
    with open(filename) as fin, open('TRAIN_3_tags_with_title.csv','w') as fw:
        fw.write(prefix_train+'\n')
        for item in fin:
            fw.write(item)

def remove_title(filename):
    with open(filename) as fin,open('TEST_3_textrank_without_title.csv','w') as fw:
        fin.readline()
        for item in fin:
            fw.write(item)

def convert_csv_txt(filename):
    wfilename = filename.replace('.csv','.txt')
    with open(filename) as fin,open(wfilename,'w') as fw:
        fin.readline()
        for item in fin:
            item_list = item.decode('utf-8').split(',')
            fw.write(' '.join(item_list).encode('gb18030'))

def convert_separate_line(filename):
    wfilename = filename.replace('.csv','_separate.csv')
    with open(filename) as fin, open(wfilename,'w') as fw:
        all_decode = fin.readline().strip().decode('gbk')
        index = 0
        count = 0
        while count < 20000:
            fw.write(all_decode[index:index+38].encode('gbk')+'\n')
            index+=38
            count+=1
            print index

def convert_txt_csv(filename):
    wfilename = filename.replace('.txt','.csv')
    with open(filename) as fin, open(wfilename,'w') as fw:
        #fw.write('id,age,gender,education,query_list\n')
        fw.write('id,query_list\n')
        for item in fin:
            item_list = item.decode('gb18030').split()
            fw.write(item_list[0].encode('utf-8')+','+' '.join(item_list[1:]).encode('utf-8')+'\n')


if __name__ == '__main__':
    #add_title('TRAIN_3_tags.csv')
    #remove_title('TRAIN_3_textrank.csv')
    #remove_title('TEST_3_textrank.csv')
    # convert_csv_txt('TEST_3_textrank_without_title.csv')
    # convert_csv_txt('TRAIN_4_tag_with_unknown.csv')
    #convert_separate_line('result_5_custom_without_unknown_svm_linear.csv')
    convert_txt_csv('./1102特征选择/test_data_fenci.txt')
