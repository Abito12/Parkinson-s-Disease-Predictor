import os
import math
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.svm import SVC
from Preprocess import preprocess
from sklearn.ensemble import RandomForestClassifier

#Obtain training and testing data
np_features_train, np_features_test, np_labels_train, np_labels_test = preprocess("IRIS")

#kmeans = KMeans(n_clusters = 2).fit(np_features_train)

#for feature in np_features_test:
#    print feature


#Create Naive Bayesian Model
clfNB = GaussianNB()
# Training the N-B Model
clfNB.fit(np_features_train, np_labels_train)
#Testing the N_B Model
predNB = clfNB.predict(np_features_test)

print("Using Naive Bayes Model\n")
correct_count = 0
for i in range(0, len(predNB)):
    if(np_labels_test[i] == predNB[i]):
        correct_count += 1
print("No of correct predictions = %s\nNo of test instances = %s\n\n" %(correct_count, len(predNB)))


clfSVC = SVC()
clfSVC.fit(np_features_train, np_labels_train)
predSVC = clfSVC.predict(np_features_test)
print("Using Support Vector Machine\n")
correct_count = 0
for i in range(0, len(predSVC)):
    if(np_labels_test[i] == predSVC[i]):
        correct_count +=
print("No of correct predictions = %s\nNo of test instances = %s\n\n" %(correct_count, len(predSVC)))


clfRF = RandomForestClassifier(n_estimators = 100)
clfRF.fit(np_features_train, np_labels_train)
predRF = clfRF.predict(np_features_test)
print("Using Random Forest Classifier\n")
correct_count = 0
for i in range(0, len(predRF)):
    if(np_labels_test[i] == predRF[i]):
        correct_count += 1
print(predRF)
print(np_labels_test)
print("No of correct predictions = %s\nNo of test instances = %s\n\n" %(correct_count, len(predRF)))
