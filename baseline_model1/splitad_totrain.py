# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:05:38 2016

@author: paddy
"""
#split2trainNtest("plat_adid_train.csv", "split_train_ad.csv", "split_test_ad.csv")

def split2train(inpu,train,test):
    tra = open(train,'w')
    tes = open(test,'w')
    f = open(inpu)
    
    i = 0
    while True:
        line = f.readline()
        INDEX,AD,CLICK,PLATFORM = line.split(',')
        i = int(INDEX)
        if i > 11812215:
            break
        tra.write(line)
    tra.close()
    
    while True:
        line = f.readline()
        if line == "" :
            break
        INDEX,AD,CLICK,PLATFORM = line.split(',')
        i = int(INDEX)
        tes.write(line)
    tes.close
split2train("plat_adid_train.csv","split_train_ad.csv","split_test_ad.csv")