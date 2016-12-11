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
        #read next line of events if changed displayid
        if displayIdListIdx != previousDisplayId:
            previousDisplayId = displayIdListIdx #count++
            #update the event line
            line2 = in2.readline()
            displayIdListIdx2,uuid,document,times,platform,geo = line2.split(',')
        
        
        i = int(displayIdListIdx)
        i2 = int(displayIdListIdx2)
        
        if click == 1:
        	#write geo and ad_id to outputfile
        	combi = str(displayIdListIdx) +','+str(ad_id)+','+str(geo)+'\n'
        	out.write(combi)
        	