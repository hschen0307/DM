# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:48:27 2016

@author: paddy
"""
def combineFea(inFile1,inFile2,outFile):
    in1 = open(inFile1,'r')
    in2 = open(inFile2,'r')
    out = open(outFile,'w')
    
    in1.readline()
    in2.readline()
    previousDisplayId = 1
    
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
        
        click = int(click)
        if click == 1:
        	#write geo and ad_id to outputfile
            combi = displayIdListIdx +','+ad_id+','+platform+'\n'
            out.write(combi)

    in1.close()
    in2.close()
    out.close()

combineFea('clicks_train.csv','events.csv','plat_adid.csv')
#undone