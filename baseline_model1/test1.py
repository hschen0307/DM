# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:55:14 2016

@author: paddy
"""
def split2trainNtest(inputFile, outputTrain, outputTest):
	train = open(outputTrain, 'w')
	test = open(outputTest, 'w')
	f = open(inputFile)
	f.readline()  # skip header

	# create list to hold all displayid (total = 16874593) 70 % = 11812215

	i=0
	while(True):
		line = f.readline()
		displayIdListIdx, ad_id, click = line.split(',')
  
		i = int(displayIdListIdx)
		if(i > 11812215): 
			break
		train.write(line)
		
	train.close()

	while(True):
		line = f.readline()
		if (line ==""):
			break
		displayIdListIdx, ad_id, click = line.split(',')
		i = int(displayIdListIdx)
		test.write(line)
		
	test.close()

split2trainNtest("clicks_train.csv", "split_train.csv", "split_test.csv")