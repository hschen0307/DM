import time
import numpy as np
import scipy.sparse as ss
from sklearn.metrics import pairwise_distances
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# Max Ad_id = 548019

def topN (a,N):
	return np.argsort(a)[:N]

def save2sparse(inputFile):

	row = []
	col = []
	data = []
	ans = []
	ans.append(-1)

	f = open(inputFile, 'r')
	f.readline()  #skip header

	# create list to hold all displayid (total = 11812215) 70 % = 11812215
	start = time.time()
	for line in f:

		# parse input
		dis_id, ad_id, click = line.split(',')

		dis_id  = int(dis_id)
		ad_id = int(ad_id)
		click = int(click)
		
		row.append(dis_id)
		col.append(ad_id)
		data.append(1)

		# save to dict
		if(click == 1):
			ans.append(ad_id)

	trainMat = ss.csr_matrix((data, (row, col)))

	#print type(trainMat)
	end = time.time()
	print "time used to read: " , end - start
	return trainMat, ans

# save2sparse("clicks_train.csv")

def predictAll(full, ans, nNear, randomNum):

	train, test, trainAns, testAns = train_test_split(full, ans, test_size=0.3, random_state=randomNum)


	dist = pairwise_distances(test,train,'cosine')

	# go throught test row by row
	accu = 0
	for cur in range(test.shape[0]):

		nearNeiborIdx = topN (dist[cur],nNear)

		# save possible ans to list
		ansList = []
		for x in nearNeiborIdx:
			ansList.append(trainAns[x])
		
		# go through actual appear ad and select top occurence in possible ans list

		cx = test[cur].tocoo()    
		if (len(cx.col) != 0):
			prediction = cx.col[0]
		occu = 0
		for ad_id  in cx.col:
			if(ansList.count(ad_id)>occu):
				occu = ansList.count(ad_id)
				prediction = ad_id
	   	
	   	if prediction == testAns[cur]:
	   		accu += 1

	return float(accu)/test.shape[0]

def repetedPrediction():
	full, ans = save2sparse("small_full.csv")
	avg = []
	for x in range(5):
		avg.append(predictAll(full, ans, 1, x))

	print avg
	print sum(avg)/len(avg)

repetedPrediction()