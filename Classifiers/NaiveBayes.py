import time
import sys
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import Helper

sys.path.append('../')
from Preprocess import preprocess


# Model Attributes
predTH = 0.5
showDetails = True

#Create Naive Bayesian Model
clf = GaussianNB()
print("\nNaive Bayesian Classification Model")
print("````````````````````````````````````````")


score = 0
timeC = 0


for user in Helper.Users:
    print(user)
    #Obtain training and testing data
    np_features_train, np_features_test, np_labels_train, np_labels_test = preprocess(user)
    pdscore = np_labels_test[0]

    # Training the N-B Model
    training_start_time = time.clock()
    clf.fit(np_features_train, np_labels_train)
    timeC += time.clock() - training_start_time


    #Testing the N_B Model
    predNB = clf.predict(np_features_test)
    print(np_labels_test)
    print(predNB)

    temp = np.full(len(np_labels_test), 1)
    pred_value = accuracy_score(temp, predNB)

    predPD = 1 if pred_value >= predTH else 0

    if predPD == pdscore:
        score += 1
    if(showDetails):
        print("User : %s (%s)" %(user, Helper.status[pdscore]))
        print("Fraction of instances indicating PD = " + str(pred_value))
        print("Prediction : " + Helper.status[predPD])
        print("\n")


print("Training took %s seconds" %(timeC))
print ("Number of correctly classified subjects = %s\n" %(score))
