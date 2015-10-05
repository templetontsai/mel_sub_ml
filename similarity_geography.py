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
    population_d = all_sub_features['Population Density']
    area = all_sub_features['Area (km^2)']
    population_d = population_d.values.tolist()
    area = area.values.tolist()

    for i in range(len(population_d)):
        population_d[i] = float(population_d[i])

    for i in range(len(area)):
        area[i] = float(area[i])

    population_d = preprocessing.normalize(population_d)
    area = preprocessing.normalize(area)
    
    population_d = population_d.tolist()[0]
    area = area.tolist()[0]
    id_features = []

    for i in range(34):
        id_features.append([population_d[i], area[i]])
    return id_features

def distance_metrix():
    sm_m = init()
    m = []

    for i in range(34):
        for j in range(34):
	    m.append(sm.euclidean_distance([sm_m[i][0], sm_m[i][1]], 
			[sm_m[j][0], sm_m[j][1]]))
    return m

def similarity_geography(sub_a, sub_b):
    id_features = init()
    return similarity_sub([id_features[sub_a][0], id_features[sub_a][1]],
	    [id_features[sub_b][0], id_features[sub_b][1]])


#sub_a = int(sys.argv[1]) - 1
#sub_b = int(sys.argv[2]) - 1
print similarity_geography(9, 14)
