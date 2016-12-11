# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:24:09 2016

@author: paddy
"""
import matplotlib.pyplot as plt
import numpy as np

ans = []
howmany =[]
def findpopularadforplot(infile):
    infile = open(infile,'r')
    for line in infile:
        AD_ID, TIMES = line.split(',')
        TIMES = int(TIMES)
        if TIMES > 35000:
            ans.append(AD_ID)
            howmany.append(TIMES)
        
    return ans,howmany
    
x = findpopularadforplot('AdOccurTimes.csv')
print x

