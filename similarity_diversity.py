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
import similarity_measure as sm


def similarity_sub(a, b):
    return sm.jaccard_similarity(a, b)

sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1
all_sub_features = pd.read_csv('all_sub_all_category.csv')
sub_id = all_sub_features['ID']
sub_id = sub_id.values.tolist()
heading = ['Top country of birth', '2nd top country of birth', '3rd top country of birth', '4th top country of birth', '5th top country of birth']
id_features = []
rank_1st = all_sub_features['Top country of birth']
rank_1st = rank_1st.tolist()
rank_2nd = all_sub_features['2nd top country of birth']
rank_2nd = rank_2nd.tolist()
rank_3rd = all_sub_features['3rd top country of birth']
rank_3rd = rank_3rd.tolist()
rank_4th = all_sub_features['4th top country of birth']
rank_4th = rank_4th.tolist()
rank_5th = all_sub_features['5th top country of birth']
rank_5th = rank_5th.tolist()

lan_1st = all_sub_features['Top language spoken']
lan_1st = lan_1st.tolist()
lan_2nd = all_sub_features['2nd top language spoken']
lan_2nd = lan_2nd.tolist()
lan_3rd = all_sub_features['3rd top language spoken']
lan_3rd = lan_3rd.tolist()
lan_4th = all_sub_features['4th top language spoken']
lan_4th = lan_4th.tolist()
lan_5th = all_sub_features['5th top language spoken']
lan_5th = lan_5th.tolist()

for i in range(34):
    id_features.append([sub_id[i], rank_1st[i].rstrip(),rank_2nd[i].rstrip(), rank_3rd[i].rstrip(), rank_4th[i].rstrip(), rank_5th[i].rstrip(),
	    lan_1st[i].rstrip(), lan_2nd[i].rstrip(), lan_3rd[i].rstrip(), lan_4th[i].rstrip(), lan_5th[i].rstrip()])
'''
for i in range(34):
    for j in range(34):
        print similarity_sub(id_features[i][1:], id_features[j][1:])
'''
print similarity_sub(id_features[sub_a][1:], id_features[sub_b][1:])
