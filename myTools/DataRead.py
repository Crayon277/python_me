#!/usr/bin/env python
# coding=utf-8

def transcsv2dicBYtitle(filename,sep=',',enc='utf-8'):
    '''
    The first line in csv is title, followd by several lines indicates data. de-/encoding default set to utf-8
    Default seperate is comma. Specify if space.

    a | b | c    (title)
    -- --- --
    1 | 2 | 3
    -- --- --
    4 | 5 | 6
    ...

    dic will be {a:[1,4],b:[2,5],c:[3,6]} They are All str!!
    '''
    dic={}
    try:
        with open(filename) as fread:
            title = fread.readline().decode(enc).strip().split(sep)
            for data_line in fread:
                data_line_decode_list = data_line.decode(enc).strip().split(sep)
                for index,data in enumerate(data_line_decode_list):
                        l=dic[title[index].encode(enc)]=dic.get(title[index].encode(enc),[])
                        #In order to let l and dic[] point the same value. Then we can change dic[] by changing l.
                        #Notice that * of dic[*] are as same as * of dic.get(*,)
                        l.append(data.encode(enc))
        print dic
    except IOError as e:
        print 'File Error',e
    else:
        return dic

def transcsv2dicBYTable(filename,sep=',',enc='utf-8'):
    '''
      | a | b | c |
    -- --- --- ---
    m | 2 | 3 | 4 |
    -- --- --- ---
    n | 5 | 6 | 7 |

    -->

    users={
        'a':{'m':2,'n':5},
        'b':{'m':3,'n':6},
        'c':{'m':4,'n',7}
    }
    '''
    dic = {}
    try:
        with open(filename) as fread:
            first_line = fread.readline().decode(enc).strip().split(sep)
            first_line.pop(0)

            for data_line in fread:
                data_line_decode_list = data_line.decode(enc).strip().split(sep)
                attr = data_line_decode_list.pop(0)
                index = 0
                for name in first_line:
                    dd=dic[name.encode(enc)]=dic.get(name.encode(enc),{})
                    if data_line_decode_list[index] == '-':
                        pass
                    else:
                        dd[attr.encode(enc)] = float(data_line_decode_list[index])
                    index+=1
        print dic
        return dic

    except Exception as e:
        raise

if __name__ == '__main__':
    # trans_csv2dic('test.csv')
    # print '='*10
    # trans_csv2dic('test_2.csv')
    print '*'*10
    transcsv2dicBYTable('test3.csv')
