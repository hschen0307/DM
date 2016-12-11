# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:35:07 2016

@author: paddy
"""

def combineFea(inFile1,inFile2,outFile):
    in1 = open(inFile1,'r')
    in2 = open(inFile2,'r')
    out = open(outFile,'w')
    
    in1.readline()
    in2.readline()
    previousDisplayId = 11812216
    
    #initial the first events data line
    line2 = in2.readline()
    displayIdListIdx2,uuid,document,times,platform,geo = line2.split(',')
    while(True):
        
        line1 = in1.readline()
        displayIdListIdx, ad_id, click = line1.split(',')
        i = int(displayIdListIdx)
        
        if(i>16874592):
            break
        #read next line of events if changed displayid
        if i != previousDisplayId:
            previousDisplayId = i #count++
            #update the event line
            line2 = in2.readline()
            displayIdListIdx2,uuid,document,times,platform,geo = line2.split(',')
        c = int(click)
        
        	#write ad_id and plat to outputfile
        combi = str(displayIdListIdx) +','+str(ad_id)+','+str(c)+','+str(times)+'\n'
        if int(click) == 1:
            out.write(combi)

    in1.close()
    in2.close()
    out.close()

combineFea('clicks_train.csv','events.csv','time_adid.csv')
#undone