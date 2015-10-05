#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import pandas as pd
from pandas import *
import csv
import sys
import locale
from sklearn import preprocessing

all_sub_features = pd.read_csv('all_sub_all_category.csv')

x_label = sys.argv[1]
y_label = sys.argv[2]

is_normalized = sys.argv[3]
is_standardized = sys.argv[4]

x = all_sub_features[x_label]
y = all_sub_features[y_label]
x = x.values.tolist()
y = y.values.tolist()


for i in range(len(x)):
    x[i] = float(x[i])

for i in range(len(y)):
    y[i] = float(y[i])

if(is_normalized == '1'):
    x = preprocessing.normalize(x)
    y = preprocessing.normalize(y)
#    print x
#    print y

if(is_standardized == '1'):
    x = preprocessing.scale(x)
    y = preprocessing.scale(y)
#    print x
#    print y

sub_name = all_sub_features['Name']
sub_id = all_sub_features['ID']
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.scatter(x, y)
#for i, txt in enumerate(sub_id):
# plt.annotate(txt, (x[i], y[i]))


plt.show()
