with open('TRAIN_4_tag_without_unknown.csv') as fin, open('TRAIN_4_tag_without_unknown.txt','w') as fw:
    fin.readline()
    for item in fin:
        item_list = item.decode('utf-8').strip().split(',')
        fw.write(item_list[0].encode('gb18030')+' '+item_list[1].encode('gb18030')+' '+item_list[2].encode('gb18030')+' '+item_list[3].encode('gb18030')+' '+item_list[4].encode('gb18030')+'\n')

# with open('TEST_3_tags.csv') as fintest, open('TEST_3_tags_zhangle.txt','w') as fwtest:
    # fintest.readline()
    # for item in fintest:
        # item_list = item.decode('utf-8').strip().split(',')
        # fwtest.write(item_list[1].encode('gb18030')+' '+item_list[2].encode('gb18030')+'\n')
