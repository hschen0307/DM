# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:22:43 2016

@author: paddy
"""

def timeswithplat(platandid,output1,output2,output3):
    output1 = open(output1,'w')
    output2 = open(output2,'w')
    output3 = open(output3,'w')
    filee = open(platandid,'r')
    
    plat1={}
    plat2={}
    plat3={}
    
    for line in filee:
        INDEX,AD,CLICKED,PLAT = line.split(',')
        AD = int(AD)
        click = int(CLICKED)
        PLAT = PLAT.replace('\\N\n','')
        if PLAT != '':    
            platform = int(PLAT)

        if click == 1:
            if platform == 1:
                if AD in plat1:
                    plat1[AD] += 1
                else:
                    plat1[AD]=1
            if platform == 2:
                if AD in plat2:
                    plat2[AD] += 1
                else:
                    plat2[AD]=1
            if platform == 3:
                if AD in plat3:
                    plat3[AD] += 1
                else:
                    plat3[AD]=1
    for ad,times in plat1.items():
        line = str(ad)+','+str(times)+'\n'
        output1.write(line)
    for ad,times in plat2.items():
        line = str(ad)+','+str(times)+'\n'
        output2.write(line)
    for ad,times in plat3.items():
        line = str(ad)+','+str(times)+'\n'
        output3.write(line)
    
def predict(test,out1,out2,out3):
    tfile = open(test,'r')
    out1 = open(out1,'r')
    out2 = open(out2,'r')
    out3 = open(out3,'r')
    
    plat1={}
    plat2={}
    plat3={}
    for line in out1:
        ad,times = line.split(',')
        plat1[int(ad)] = int(times)
    for line in out2:
        ad,times = line.split(',')
        plat2[int(ad)]=int(times)
    for line in out3:
        ad,times = line.split(',')
        plat3[int(ad)]=int(times)
    out1.close()
    out2.close()
    out3.close()
    
    CORRECT_COUNT = 0
    ans = {}
    plats={}
    doc = {}
    while(True):
        line = tfile.readline()
        if (line==""):
            break
        # read test
        INDEX,AD_ID,CLICKED,PLATFORM = line.split(',')
        PLATFORM = PLATFORM.replace('\\N\n','')
        if PLATFORM != '':
            PLAT = int(PLATFORM)
        IN = int(INDEX)
        AD = int(AD_ID)
        click = int(CLICKED)
        if IN in doc:
            doc[IN].append(AD)
        else:
            doc[IN] = [AD]
            plats[IN] = PLAT
        if click == 1:
            ans[IN] = AD_ID


    for doc_id, adlist in doc.items():
        temp = {}
        for ad_id in adlist:
            platnum = int(plats[int(doc_id)])
            if platnum ==1:
                if ad_id in plat1:
                    temp[ad_id] = plat1[ad_id]
                else:
                    temp[ad_id] = 0
            elif platnum ==2:
                if ad_id in plat2:
                    temp[ad_id] = plat2[ad_id]
                else:
                    temp[ad_id] =0         
            elif platnum ==3:
                if ad_id in plat3:
                    temp[ad_id] = plat3[ad_id]
        maxAd=0
        maxtimes = 0
        for ad_id, times in temp.items():
            if times > maxtimes:
                maxAd = ad_id
                maxtimes = times
        #print (maxAd) , (ans[doc_id])
        #print type(maxAd)
        #print type(ans[doc_id])
        #print CORRECT_COUNT
        if maxAd-int(ans[doc_id])==0:
            CORRECT_COUNT += 1
        
    correctness = float(CORRECT_COUNT)/len(ans)
    print correctness
#timeswithplat('split_train_ad.csv','plat1.csv','plat2.csv','plat3.csv')
predict('split_test_ad.csv','plat1.csv','plat2.csv','plat3.csv')
        
            