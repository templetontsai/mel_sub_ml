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

def similarity_sub_coef(a, b, a_coef, b_coef):
    return (sm.jaccard_similarity(a, b) + sm.dis_to_sim(sm.euclidean_distance(a_coef, b_coef)))/2
sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1

all_sub_features = pd.read_csv('all_sub_all_category.csv')

sub_id = all_sub_features['ID']
sub_id = sub_id.values.tolist()
id_features = []
id_features_p = []

birth_1st = all_sub_features['Top country of birth']
birth_1st = birth_1st.tolist()
birth_2nd = all_sub_features['2nd top country of birth']
birth_2nd = birth_2nd.tolist()
birth_3rd = all_sub_features['3rd top country of birth']
birth_3rd = birth_3rd.tolist()
birth_4th = all_sub_features['4th top country of birth']
birth_4th = birth_4th.tolist()
birth_5th = all_sub_features['5th top country of birth']
birth_5th = birth_5th.tolist()

birth_1st_p = all_sub_features['Top country of birth, %']
birth_1st_p = preprocessing.normalize(birth_1st_p.values.tolist())[0]
birth_2nd_p = all_sub_features['2nd top country of birth, %']
birth_2nd_p = preprocessing.normalize(birth_2nd_p.values.tolist())[0]
birth_3rd_p = all_sub_features['3rd top country of birth, %']
birth_3rd_p = preprocessing.normalize(birth_3rd_p.values.tolist())[0]
birth_4th_p = all_sub_features['4th top country of birth, %']
birth_4th_p = preprocessing.normalize(birth_4th_p.values.tolist())[0]
birth_5th_p = all_sub_features['5th top country of birth, %']
birth_5th_p = preprocessing.normalize(birth_5th_p.values.tolist())[0]


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

lan_1st_p = all_sub_features['Top language spoken, %']
lan_1st_p = preprocessing.normalize(lan_1st_p.values.tolist())[0]
lan_2nd_p = all_sub_features['2nd top language spoken, %']
lan_2nd_p = preprocessing.normalize(lan_2nd_p.values.tolist())[0]
lan_3rd_p = all_sub_features['3rd top language spoken, %']
lan_3rd_p = preprocessing.normalize(lan_3rd_p.values.tolist())[0]
lan_4th_p = all_sub_features['4th top language spoken, %']
lan_4th_p = preprocessing.normalize(lan_4th_p.values.tolist())[0]
lan_5th_p = all_sub_features['5th top language spoken, %']
lan_5th_p = preprocessing.normalize(lan_5th_p.values.tolist())[0]


for i in range(34):
    id_features.append([sub_id[i], birth_1st[i].rstrip(),birth_2nd[i].rstrip(), birth_3rd[i].rstrip(), birth_4th[i].rstrip(), birth_5th[i].rstrip(),
	    lan_1st[i].rstrip(), lan_2nd[i].rstrip(), lan_3rd[i].rstrip(), lan_4th[i].rstrip(), lan_5th[i].rstrip()])

for i in range(34):
    id_features_p.append([sub_id[i], birth_1st_p[i], birth_2nd_p[i], birth_3rd_p[i], birth_4th_p[i], birth_5th_p[i],
	    lan_1st_p[i], lan_2nd_p[i], lan_3rd_p[i], lan_4th_p[i], lan_5th_p[i]])

print similarity_sub(id_features[sub_a][1:], id_features[sub_b][1:])
print similarity_sub_coef(id_features[sub_a][1:], id_features[sub_b][1:], id_features_p[sub_a][1:], id_features_p[sub_b][1:])
'''
for i in range(34):
    for j in range(34):
        print similarity_sub(id_features[i][1:], id_features[j][1:])
'''
