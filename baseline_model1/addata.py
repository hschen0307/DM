# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:11:02 2016

@author: paddy
"""

#build csv into sparse matrix
occur = {}
real = {}
def addata(infile):
    infile = open(infile,'r')
    infile.readline()
    key = 11812216
    for display in range(10): # range change into all file
        line = infile.readline()
        displayIdListIdx, ad_id, click = line.split(',')
        ad_id = int(ad_id)
        click = int(click)
        if displayIdListIdx == key:
            if (click==1):
                occur[ad_id] = 1
            else:
                occur[ad_id] = 0
        else:            
            real[key] = occur
            key = int(displayIdListIdx)
            if (click==1):
                occur[ad_id] = 1
            else:
                occur[ad_id] = 0
            
    return real
    
x = addata('split_test.csv') # change into train file

print x
