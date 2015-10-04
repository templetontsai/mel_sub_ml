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
#return sm.dis_to_sim(sm.euclidean_distance(a, b))
#    return sm.dis_to_sim(sm.manhattan_distance(a, b))
#    return sm.dis_to_sim(sm.minkowski_distance(a, b, 3))
    return sm.dis_to_sim(sm.cosine_similarity(a, b))


all_sub_features = pd.read_csv('all_sub_all_category.csv')

sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1

#travel_t = all_sub_features['Travel time to GPO (minutes)']
population_d = all_sub_features['Population Density']
area = all_sub_features['Area (km^2)']

#travel_t = travel_t.values.tolist()
population_d = population_d.values.tolist()
area = area.values.tolist()
sub_id = all_sub_features['ID']
sub_id = sub_id.values.tolist()
'''
for i in range(len(travel_t)):
    travel_t[i] = float(travel_t[i])
'''
for i in range(len(population_d)):
    population_d[i] = float(population_d[i])

for i in range(len(area)):
    area[i] = float(area[i])

#travel_t = preprocessing.normalize(travel_t)
population_d = preprocessing.normalize(population_d)
area = preprocessing.normalize(area)
'''
if(is_standardized == '1'):
    x = preprocessing.scale(x)
    y = preprocessing.scale(y)
'''
#travel_t = travel_t.tolist()[0]
population_d = population_d.tolist()[0]
area = area.tolist()[0]
id_features = []
for i in range(34):
    id_features.append([sub_id[i], population_d[i], area[i]])

print similarity_sub([id_features[sub_a][1], id_features[sub_a][2]],
	[id_features[sub_b][1], id_features[sub_b][2]])
'''
id_features.append([sub_id[i], travel_t[i], population_d[i], area[i]])
print similarity_sub([id_features[sub_a][1], id_features[sub_a][2], id_features[sub_a][3]],
	[id_features[sub_b][1], id_features[sub_b][2], id_features[sub_b][3]])
'''

