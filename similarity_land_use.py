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
    return sm.dis_to_sim(sm.euclidean_distance(a, b))
#    return sm.dis_to_sim(sm.manhattan_distance(a, b))
#    return sm.dis_to_sim(sm.minkowski_distance(a, b, 3))
#    return sm.dis_to_sim(sm.cosine_similarity(a, b))

def init():
    all_sub_features = pd.read_csv('all_sub_all_category.csv')

    c_land = sm.to_nomalized(sm.to_float(all_sub_features['Commercial (%)'].tolist())).tolist()[0]
    i_land = sm.to_nomalized(sm.to_float(all_sub_features['Industrial (%)'].tolist())).tolist()[0]
    re_land = sm.to_nomalized(sm.to_float(all_sub_features['Residential (%)'].tolist())).tolist()[0]
    ru_land = sm.to_nomalized(sm.to_float(all_sub_features['Rural (%)'].tolist())).tolist()[0]
    
    id_features = []

    for i in range(34):
        id_features.append([c_land[i], i_land[i], re_land[i], ru_land[i]])
    return id_features

def distance_metrix():
    sm_m = init()
    m = []

    for i in range(34):
        for j in range(34):
	    m.append(sm.euclidean_distance([sm_m[i][0], sm_m[i][1], sm_m[i][2], sm_m[i][3]],
			[sm_m[j][0], sm_m[j][1], sm_m[j][2], sm_m[j][3]]))
    return m

def similarity_land_use(sub_a, sub_b):
    id_features = init()
    return similarity_sub([id_features[sub_a][0], id_features[sub_a][1], id_features[sub_a][2], id_features[sub_a][3]],
	    [id_features[sub_b][0], id_features[sub_b][1], id_features[sub_b][2], id_features[sub_b][3]])


sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1
print similarity_land_use(sub_a, sub_b)
