install.packages("knitr")
install.packages("RPostgreSQL")
install.packages('randomForest', repos="http://cran.r-project.org")
install.packages("ROCR", dep = TRUE)
install.packages("ggplot2")
library(knitr)            
library(ggplot2)
library(ROCR)
library(randomForest)
require("RPostgreSQL")    
require(randomForest)     
require(knitr)
require("ROCR")


#connect to database
connection <- dbConnect(dbDriver("PostgreSQL"), dbname = "haha",
                        host = "localhost", port = 5432,
                        user = "postgres", password = "2wsx@WSX")


#get our data from db (join related attributes)
query = "
select t.display_id, t.ad_id, t.clicked, d.topic_id, d.document_id, d.confidence_level, p.campaign_id,p.advertiser_id
from clicks_train t, promoted_content p, documents_topics d
where t.ad_id = p.ad_id and p.document_id = d.document_id
limit 600000;"


#build a new table for the data we just got  
allData=dbGetQuery(connection, query)


#plots of the data
g <- ggplot(allData)
g +  geom_bar(aes(x=clicked))
g + geom_histogram(aes(x=confidence_level),binwidth = 0.01) + facet_grid(clicked~.)
g + geom_histogram(aes(x=advertiser_id),binwidth =50 ) + facet_grid(clicked~.)
g + geom_histogram(aes(x=topic_id),binwidth = 5) + facet_grid(clicked~.)
g + geom_histogram(aes(x=campaign_id),binwidth=400) + facet_grid(clicked~.)


# balanced data set (50 clicked, 50 not-clicked)
click_set = subset(allData, clicked>0) #get all clicked rows 
nonClick_all = subset(allData, clicked < 1) #get all not-clicked rows 
nonClick_set = nonClick_all[sample(nrow(nonClick_all), 64352),] #same size as clicked 
balance_set <- merge(click_set, nonClick_set, all.x=TRUE, all.y=TRUE)


#Training set and test set
training_size = floor(0.80 * nrow(balance_set)) #set the size of training
set.seed(123) #make sampleing different at each time
training_index <- sample(seq_len(nrow(balance_set)), size = training_size)


# sample training set
train_set <- balance_set[training_index, ]
train_set = sample(train_set, length(train_set))


# sample test set
test_set <- balance_set[-training_index, ]
test_set = sample(test_set, length(test_set))


#Radom forest
#using confidence_level features
#accuracy(AVE) 64%
rfmodel=randomForest(clicked ~ confidence_level+topic_id, data=train_set, ntree=1)
rfmodel.probs=predict(rfmodel,test_set)
rfmodel.pred=ifelse(rfmodel.probs>0.5,1,0)
table(rfmodel.pred, test_set$clicked)
rf_acc1 = mean(rfmodel.pred == test_set$clicked)     # numberic accuracy
rf_acc1 

rfmodel=randomForest(clicked ~ confidence_level+topic_id, data=train_set, ntree=10)
rfmodel.probs=predict(rfmodel,test_set)
rfmodel.pred=ifelse(rfmodel.probs>0.5,1,0)
table(rfmodel.pred, test_set$clicked)
rf_acc2 = mean(rfmodel.pred == test_set$clicked)     # numberic accuracy
rf_acc2

rfmodel=randomForest(clicked ~ confidence_level+topic_id, data=train_set, ntree=300)
rfmodel.probs=predict(rfmodel,test_set)
rfmodel.pred=ifelse(rfmodel.probs>0.5,1,0)
table(rfmodel.pred, test_set$clicked)
rf_acc3 = mean(rfmodel.pred == test_set$clicked)     # numberic accuracy
rf_acc = (rf_acc1+rf_acc2+rf_acc3)/3


#Linear regression 1
#using features: confidence_level features
#accuracy: 57%
lrmodel=glm(clicked ~ confidence_level, data=train_set,family=binomial)
lrmodel.probs=predict(lrmodel,newdata=test_set,type="response") 
lrmodel.pred=ifelse(lrmodel.probs >0.5,1,0)
table(lrmodel.pred,test_set$clicked)
lr_acc1=mean(lrmodel.pred==test_set$clicked)     # numberic accuracy
lr_acc1


#Linear regression 2
#using using features: confidence_leve+topic_id features 
#accuracy: 59%
lrmodel=glm(clicked ~ topic_id+confidence_level, data=train_set,family=binomial)
lrmodel.probs=predict(lrmodel,newdata=test_set,type="response") 
lrmodel.pred=ifelse(lrmodel.probs >0.5,1,0)
table(lrmodel.pred,test_set$clicked)
lr_acc2=mean(lrmodel.pred==test_set$clicked)     # numberic accuracy
lr_acc2


#Linear regression 3
#using using features: confidence_level+topic_id+advertiser_id features 
#accuracy: 62%
lrmodel=glm(clicked ~ topic_id+confidence_level+advertiser_id, data=train_set,family=binomial)
lrmodel.probs=predict(lrmodel,newdata=test_set,type="response") 
lrmodel.pred=ifelse(lrmodel.probs >0.5,1,0)
table(lrmodel.pred,test_set$clicked)
lr_acc3=mean(lrmodel.pred==test_set$clicked)     # numberic accuracy
lr_acc3


#Linear regression 4
#using using features: confidence_level+topic_id+advertiser_id+campaign_id features 
#accuracy: 62%
lrmodel=glm(clicked ~ topic_id+confidence_level+advertiser_id+campaign_id, data=train_set,family=binomial)
lrmodel.probs=predict(lrmodel,newdata=test_set,type="response") 
lrmodel.pred=ifelse(lrmodel.probs >0.5,1,0)
table(lrmodel.pred,test_set$clicked)
lr_acc4=mean(lrmodel.pred==test_set$clicked)     # numberic accuracy
lr_acc4


#final result plot
allAcc <- c(rf_acc1, lr_acc1, lr_acc2,lr_acc3, lr_acc4)
barplot(allAcc, main="Accuracy Comparison", xlab="Models", ylab="Accuracy", names.arg=c("radomForest","lr1","lr2","lr3","lr4"))





