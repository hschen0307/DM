# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:11:39 2016

@author: paddy
"""
occur = {}
def adoccur(filee,outfile):
    ofile = open(filee,'r')
    out = open(outfile,'w')
    ofile.readline()
    for line in ofile:
        INDEX, ad, click = line.split(',')
        click = int(click)
        ad = int(ad)
        
        if click == 1:
            if ad in occur:
                occur[ad] +=1
            else:
                occur[ad] = 1
                
        
    
    
    for add,time in occur.items():
        string = str(add) +','+str(time)+'\n'
        out.write(string)
        
adoccur('clicks_train.csv','AdOccurTimes.csv')