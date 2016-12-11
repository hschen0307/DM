def split2trainNtest(inputFile, outputTrain, outputTest):
	train = open(outputTrain, 'w')
	test = open(outputTest, 'w')
	f = open(inputFile)
	# skip header

	# create list to hold all displayid (total = 16874593) 70 % = 11812215

	i=0
     while(True):
		line = f.readline()
		displayIdListIdx, ad_id, click, plat = line.split(',')
		i = int(displayIdListIdx)
		if(i > 11812215): 
			break
		train.write(line)
		
	train.close()

	while(True):
		line = f.readline()
		if (line ==""):
			break
		displayIdListIdx, ad_id, click, plat = line.split(',')
		i = int(displayIdListIdx)
		test.write(line)
		
	test.close()

split2trainNtest("plat_adid_train.csv", "split_train_ad.csv", "split_test_ad.csv")