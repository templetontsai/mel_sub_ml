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
import sys



all_sub_features = pd.read_csv('all_sub_all_category.csv')

x_label = sys.argv[1]
y_label = sys.argv[2]

x = all_sub_features[x_label]
y = all_sub_features[y_label]
sub_name = all_sub_features['Name']
sub_id = all_sub_features['ID']
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.scatter(x, y)
for i, txt in enumerate(sub_id):
    plt.annotate(txt, (x[i], y[i] ))


plt.show()
