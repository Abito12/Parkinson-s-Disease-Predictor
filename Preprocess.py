import os
import sys
import math
from datetime import datetime
import pandas as pd
import numpy as np

root = "../Aggregated_Data"

#Add all the users here
Users = [
    "APPLE","CHERRY","CROCUS","DAFODIL",
    "FLOX","IRIS","LILLY","ORANGE",
    "PEONY","ROSE","SUNFLOWER","SWEETPEA","VIOLET"
]

# Leave one out Cross Validation

def preprocess(test_subject):
    df_features_train = pd.DataFrame()
    df_features_test =  pd.DataFrame()

    for user in Users:
        path = os.path.join(root, user + "-hdl_aggregated.csv")
        # Read accel file of each user to DataFrame
        df = pd.read_csv(path,  sep='\t')
        if(user == test_subject):
            df_features_test = df_features_test.append(df, ignore_index = True)
        else:
            df_features_train = df_features_train.append(df, ignore_index = True)

    #df_features_train.to_csv('test.csv', sep='\t', encoding='utf-8')

    pds_feature_train = df_features_train['pdscore']
    np_labels_train = pds_feature_train.values

    pds_feature_test = df_features_test['pdscore']
    np_labels_test = pds_feature_test.values

    #print(df_features_train.info())
    del df_features_train['pdscore']
    del df_features_test['pdscore']
    del df_features_test['year']
    del df_features_train['year']
    del df_features_test['month']
    del df_features_train['month']
    del df_features_test['hour']
    del df_features_train['hour']
    del df_features_test['day']
    del df_features_train['day']

    np.set_printoptions(suppress=True)

    np_features_train = list(df_features_train.values)
    np_features_test = list(df_features_test.values)


    return np_features_train, np_features_test, np_labels_train, np_labels_test
