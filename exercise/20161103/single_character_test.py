#!/usr/bin/env python
# coding=utf-8

import unittest
import single_character
import graphlab

class TestSVM(unittest.TestCase):
    """docstring for ."""
    def test_svm(self):
        # filename='TRAIN_3_tags_with_title.csv'
        #data = graphlab.load_sframe('TRAIN_3_tags_with_title_save_sframe')
        data = graphlab.SFrame('TRAIN_4_tag_without_unknown.csv')
        train_data,test_data=data.random_split(.8,seed=0)
        train_data = single_character.pre_handle_data(train_data)
        single_character.main(train_data,test_data,mode = 0,unno=0)

if __name__ == '__main__':
    unittest.main()
