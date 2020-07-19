import pickle 
import pdb
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.model_selection import PredefinedSplit, GridSearchCV
from sklearn.metrics import (confusion_matrix, precision_score, recall_score, f1_score,\
                             fbeta_score, roc_auc_score, precision_recall_curve, auc,\
                             brier_score_loss)

sys.path.insert(1, '../')

from load_data import *

bin_size = 2

temp = []
for i in range(fold_1_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_1_hydrogens[i], np.r_[:fold_1_hydrogens[i].shape[0]:bin_size]))
fold_1_hydrogens = np.array(temp)

temp = []
for i in range(fold_2_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_2_hydrogens[i], np.r_[:fold_2_hydrogens[i].shape[0]:bin_size]))
fold_2_hydrogens = np.array(temp)

temp = []
for i in range(fold_3_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_3_hydrogens[i], np.r_[:fold_3_hydrogens[i].shape[0]:bin_size]))
fold_3_hydrogens = np.array(temp)

temp = []
for i in range(fold_4_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_4_hydrogens[i], np.r_[:fold_4_hydrogens[i].shape[0]:bin_size]))
fold_4_hydrogens = np.array(temp)

temp = []
for i in range(fold_5_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_5_hydrogens[i], np.r_[:fold_5_hydrogens[i].shape[0]:bin_size]))
fold_5_hydrogens = np.array(temp)

temp = []
for i in range(fold_6_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_6_hydrogens[i], np.r_[:fold_6_hydrogens[i].shape[0]:bin_size]))
fold_6_hydrogens = np.array(temp)

temp = []
for i in range(fold_7_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_7_hydrogens[i], np.r_[:fold_7_hydrogens[i].shape[0]:bin_size]))
fold_7_hydrogens = np.array(temp)

temp = []
for i in range(fold_8_hydrogens.shape[0]):
    temp.append(np.maximum.reduceat(fold_8_hydrogens[i], np.r_[:fold_8_hydrogens[i].shape[0]:bin_size]))
fold_8_hydrogens = np.array(temp)


# 8 fold cross validation
auroc_folds = []
aupr_folds = []

for test_index in [1, 2, 3, 4, 5, 6, 7, 8]:
    print()
    print("************ Test Fold " + str(test_index) + " ************")
    print()

    train_indices = list(range(1,9))
    train_indices.remove(test_index)
    print(train_indices)

    test_hydrogens = eval("fold_" + str(test_index) + "_hydrogens")
    test_labels = eval("fold_" + str(test_index) + "_labels")
    train_hydrogens_tuple = tuple([eval('fold_' + str(x) + '_hydrogens') for x in train_indices])
    train_labels_tuple = tuple([eval('fold_' + str(x) + '_labels') for x in train_indices])
    train_hydrogens = np.vstack(train_hydrogens_tuple)
    train_labels = np.vstack(train_labels_tuple)

    # scale all samples according to training set
    scaler = preprocessing.MinMaxScaler().fit(train_hydrogens)
    train_hydrogens_normalized = scaler.transform(train_hydrogens)
    test_hydrogens_normalized = scaler.transform(test_hydrogens)

    clf = SVC(C=100, gamma='scale', kernel='rbf', class_weight='balanced', probability=True)
    clf.fit(train_hydrogens_normalized, np.ravel(train_labels))

    test_pred = clf.predict(test_hydrogens_normalized)
    test_pred_prob = clf.predict_proba(test_hydrogens_normalized)
    
    cm = confusion_matrix(test_labels, test_pred)

    auroc = roc_auc_score(test_labels, test_pred_prob[:,1])
    auroc_folds.append(auroc)

    precision, recall, thresh = precision_recall_curve(test_labels, test_pred_prob[:,1])
    aupr = auc(recall, precision)
    aupr_folds.append(aupr)

    print("AUROC: ", auroc)
    print("AUPR: ", aupr)

# append metrics per fold to a run file
with open("./logs/SVM/auroc_scores.txt", "w") as f:
    for auroc in auroc_folds:
        f.write("%f\n" % (auroc))
with open("./logs/SVM/aupr_scores.txt", "w") as f:
    for aupr in aupr_folds:
        f.write("%f\n" % (aupr))  