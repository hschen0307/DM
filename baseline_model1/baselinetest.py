def saveOccurence(inputFile, outputFile):
	output = open(outputFile, 'w')
	f = open(inputFile, 'r')

	# create list to hold all displayid (total = 11812215) 70 % = 11812215

	occuDict={} 
	for line in f:

		# parse input
		displayIdListIdx, ad_id, click = line.split(',')
		ad_id = int(ad_id)
		click = int(click)
		
		# save to dict
		if(click == 1):
			if(ad_id in occuDict):
				occuDict[ad_id] += 1;
			else:
				occuDict[ad_id] = 1;

	# output to file

	for k, v in occuDict.items():
	    line = str(k) + ',' + str(v) + '\n'
	    output.write(line)
	output.close()


def predictFromFile(testFile, occuFile):
	tFile = open(testFile, 'r')
	oFile = open(occuFile, 'r')

	# read occuFile into dict
	occuDict = {}
	for line in oFile:
		ad_id, occu = line.split(',')
		occuDict[int(ad_id)] = int(occu)

	correctCount = 0
	ansDict = {}
	docDict = {}
	print "finish reading occurence"
	# read ad in same doc into list and save to dict
	while(True):
		line = tFile.readline()
		if (line ==""):
			break
		doc_id, ad_id, click = line.split(',')
		doc_id = int(doc_id)
		ad_id = int(ad_id)
		click = int(click)
		if doc_id in docDict:
			docDict[doc_id].append(ad_id)
		else:
			docDict[doc_id] = [ad_id]
		if click == 1:
			ansDict[doc_id] = ad_id

	print "finish reading testfile"
	# predict each document
	for doc_id, adList in docDict.items():
		# check each ad and find the max occu ad
		tempDict = {}
		for ad_id in adList:
			if ad_id in occuDict:
				tempDict[ad_id] = occuDict[ad_id]
			else:
				tempDict[ad_id] = 0
		maxAd = 0
		maxOccu = 0
		for ad_id, occu in tempDict.items():
			if occu > maxOccu:
				maxOccu = occu
				maxAd = ad_id
		if maxAd == ansDict[doc_id]:
			correctCount+=1

	corretness = float(correctCount)/len(ansDict)
	print corretness



saveOccurence("split_train.csv", "dummy.csv")
predictFromFile("split_test.csv", "dummy.csv")