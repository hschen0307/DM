# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:20:20 2016

@author: paddy
"""
#import panda as pd
#import sys
#reload(sys)

#sys.setdefaultencodint('utf8')
#sys.getdefaultencoding()
#def prove(filee):
 #   data = pd.read_csv(filee)

    
#prove('events.csv')

def prove(fi,testfeaEve):
    events = open(fi,'r')
    testeve = open(testfeaEve,'w')
    line = events.readline()
    
    while(True):
        line = events.readline()
        a,b,c,d,e,f = line.split(',')
        i = int(a)

        if i >16874595:
            testeve.writelines(line)
            
              #16874594
        if i >17074595:
            break
    events.close()
    testeve.close()
    
    
prove('events.csv','events_test.csv')    
