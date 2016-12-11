# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:22:52 2016

@author: paddy
"""
import matplotlib.pyplot as plt
import numpy as np

def findmax(ow):
    ads = open(ow,'r')
    ads.readline()
    adss = {}

    for line in ads:
        INDEX , CLICKED_AD, TIMESTAMP = line.split(',')#need a combine of these features

    	#find max:
        if CLICKED_AD in adss:
            adss[CLICKED_AD] +=1
        else:
            adss[CLICKED_AD] = 1
    ans = 0
    adans = 0
    for AD,times in adss.items():
    	if int(times)>ans:
    		adans = AD
    		ans = int(times)

    print "the most clicked ad is "+str(adans)+", being clicked "+str(ans)+" times"
    

#findmax("plat_adid.csv")

def AD_TIMESTAMP_PLOT(amazingfile):
	amazingfile = open(amazingfile,'r')
	x=[]
	y=[]
	numbers = 0
 	#maxclicklist = [3314, 26711, 84109, 92759, 130952, 151028, 173130, 175214, 184220, 193952, 228959, 303990]
   	maxclicklist = [3314,130952,173130,175214,303990]
	maxclick = maxclicklist[2]
	for line in amazingfile:
		INDEX,CLICKED_AD,ONE,TIMESTAMP = line.split(',')
  
		if int(CLICKED_AD) == maxclick:
			numbers +=1
   
			y.append(numbers)
			x.append(np.log(int(TIMESTAMP)))

	plt.plot(x,y)
	plt.title("AD occur times vs time in log")
		
AD_TIMESTAMP_PLOT("time_adid.csv")









    
    