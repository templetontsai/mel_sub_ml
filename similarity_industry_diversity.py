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

def similarity_sub_coef(a, b, a_coef, b_coef):
    sim_jaccard = sm.jaccard_similarity(a, b)
    sim_euclidean = sm.dis_to_sim(sm.euclidean_distance(a_coef, b_coef))
    if(sim_jaccard < 0.5):
	return sim_jaccard
    else:
        return (sm.jaccard_similarity(a, b) + sm.dis_to_sim(sm.euclidean_distance(a_coef, b_coef)))/2

def similarity_to_distance(a):
    return 1 - a

def init():
    all_sub_features = pd.read_csv('all_sub_all_category.csv')

    c_land = sm.to_nomalized(sm.to_float(all_sub_features['Commercial (%)'].tolist())).tolist()[0]
    i_land = sm.to_nomalized(sm.to_float(all_sub_features['Industrial (%)'].tolist())).tolist()[0]
    re_land = sm.to_nomalized(sm.to_float(all_sub_features['Residential (%)'].tolist())).tolist()[0]
    ru_land = sm.to_nomalized(sm.to_float(all_sub_features['Rural (%)'].tolist())).tolist()[0]
    

    indus_1st = all_sub_features['Top industry'].tolist()
    indus_2nd = all_sub_features['2nd top industry - persons'].tolist()
    indus_3rd = all_sub_features['3rd top industry - persons'].tolist()
    occup_1st = all_sub_features['Top occupation'].tolist()
    occup_2nd = all_sub_features['2nd top occupation - persons'].tolist()
    occup_3rd = all_sub_features['3rd top occupation - persons'].tolist()

    indus_1st_p = sm.to_nomalized(sm.to_float(all_sub_features['Top industry, %'].tolist())).tolist()[0]
    indus_2nd_p = sm.to_nomalized(sm.to_float(all_sub_features['2nd top industry, %'].tolist())).tolist()[0]
    indus_3rd_p = sm.to_nomalized(sm.to_float(all_sub_features['3rd top industry, %'].tolist())).tolist()[0]
    occup_1st_p = sm.to_nomalized(sm.to_float(all_sub_features['Top occupation, %'].tolist())).tolist()[0]
    occup_2nd_p = sm.to_nomalized(sm.to_float(all_sub_features['2nd top occupation, %'].tolist())).tolist()[0]
    occup_3rd_p = sm.to_nomalized(sm.to_float(all_sub_features['3rd top occupation, %'].tolist())).tolist()[0]

    id_features_land = []
    id_features_idus_occup = []
    id_features_idus_occup_p = []


    for i in range(34):
        id_features_land.append([c_land[i], i_land[i], re_land[i], ru_land[i]])

    for i in range(34):
        id_features_idus_occup.append([indus_1st[i].rstrip(), indus_2nd[i].rstrip(), indus_3rd[i].rstrip(), 
		occup_1st[i].rstrip(), occup_2nd[i].rstrip(), occup_3rd[i].rstrip()])
    
    for i in range(34):
        id_features_idus_occup_p.append([indus_1st_p[i], indus_2nd_p[i], indus_3rd_p[i], occup_1st_p[i], occup_2nd_p[i], occup_3rd_p[i]])
    id_all_features = [id_features_land, id_features_idus_occup, id_features_idus_occup_p]
    return id_all_features

def distance_metrix():
    m = []

    for i in range(34):
        for j in range(34):
	    m.append(similarity_to_distance(similarity_industry_diversity(i, j)))
    return m

def similarity_land_use(sub_a, sub_b):
    id_features = init()[0]
    return similarity_sub([id_features[sub_a][0], id_features[sub_a][1], id_features[sub_a][2], id_features[sub_a][3]],
	    [id_features[sub_b][0], id_features[sub_b][1], id_features[sub_b][2], id_features[sub_b][3]])

def similarity_idus_occup(sub_a, sub_b):
    id_all_features = init()
    id_all_features = [id_all_features[1], id_all_features[2]]


    return similarity_sub_coef(id_all_features[0][sub_a], id_all_features[0][sub_b], id_all_features[1][sub_a], id_all_features[1][sub_b])

def similarity_industry_diversity(sub_a, sub_b):
    return (similarity_land_use(sub_a, sub_b) + similarity_idus_occup(sub_a, sub_b))/2


#sub_a = int(sys.argv[1]) - 1
#sub_b = int(sys.argv[2]) - 1
#print similarity_land_use(sub_a, sub_b)
#print similarity_idus_occup(sub_a, sub_b)
#print similarity_industry_diversity(sub_a, sub_b)
