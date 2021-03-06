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
#return (sm.jaccard_similarity(a, b))
    return (sm.jaccard_similarity(a, b) + sm.dis_to_sim(sm.euclidean_distance(a_coef, b_coef)))/2

def similarity_to_distance(a):
    return 1 - a

def init():
    all_sub_features = pd.read_csv('all_sub_all_category.csv')
    id_features = []
    id_features_p = []
    id_all_features = []

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

    born_o_p = all_sub_features['Born overseas, %']
    born_o_p = preprocessing.normalize(born_o_p.values.tolist())[0]
    born_non_eng_p = all_sub_features['Born in non-English speaking country, %']
    born_non_eng_p = preprocessing.normalize(born_non_eng_p.values.tolist())[0]
    lote_p = all_sub_features['Speaks LOTE at home, %']
    lote_p = preprocessing.normalize(lote_p.values.tolist())[0]


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
        id_features.append([birth_1st[i].rstrip(),birth_2nd[i].rstrip(), birth_3rd[i].rstrip(), birth_4th[i].rstrip(), birth_5th[i].rstrip(),
	        lan_1st[i].rstrip(), lan_2nd[i].rstrip(), lan_3rd[i].rstrip(), lan_4th[i].rstrip(), lan_5th[i].rstrip()])

    for i in range(34):
        id_features_p.append([born_o_p[i], born_non_eng_p[i], lote_p[i]])

    id_all_features = [id_features, id_features_p]
    return id_all_features

def distance_metrix():
    m = []
    for i in range(34):
        for j in range(34):
	    m.append(similarity_to_distance(similarity_cultural_diversity(i, j)))
    return m

def similarity_cultural_diversity(sub_a, sub_b):
    id_all_features = init()
    return similarity_sub_coef(id_all_features[0][sub_a], id_all_features[0][sub_b], id_all_features[1][sub_a], id_all_features[1][sub_b])
    
    
#sub_a = int(sys.argv[1]) - 1
#sub_b = int(sys.argv[2]) - 1
#print similarity_cultural_diversity(sub_a, sub_b)
