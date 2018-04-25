import time
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import Helper

sys.path.append('../')
from Preprocess import preprocess


# Model Attributes
predTH = 0.5
showDetails = True

#Create Naive Bayesian Model
clf = KMeans(n_clusters = 3, random_state=0)

print("\nK-Means Clustering Model")
print("``````````````````````````````")

score = 0
timeC = 0

for user in Helper.Users:
    #Obtain training and testing data
    np_features_train, np_features_test, np_labels_train, np_labels_test = preprocess(user)
    pdscore = np_labels_test[0]

    # Training the K-Means Model
    training_start_time = time.clock()
    clf.fit(np_features_train)
    timeC += time.clock() - training_start_time

    print(clf.labels_)

    #Testing the K-Means Model
    predRF = clf.predict(np_features_test)

    temp = np.full(len(np_labels_test), 1)
    pred_value = accuracy_score(temp, predRF)


    predPD = 1 if pred_value >= predTH else 0

    if predPD == pdscore:
        score += 1
    if(showDetails):
        print("User : %s (%s)" %(user, Helper.status[pdscore]))
        print("Fraction of instances indicating PD = " + str(pred_value))
        print("Prediction : " + Helper.status[predPD])
        #print(np_labels_test)
        #print(predRF)
        print("\n")


print("Training took %s seconds" %(timeC))
print ("Number of correctly classified subjects = %s\n" %(score))
