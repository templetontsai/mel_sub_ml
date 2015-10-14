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
from math import*

def to_float(a):
    for i in range(len(a)):
        a[i] = float(a[i])
    return a

def get_table(label, table):
    table = all_sub_features[label]
    table = table.values.tolist()
    return table

def similarity_sub(a, b, num):
    return sm.dis_to_sim(sm.bhatta_distance(a, b, num))

all_sub_features = pd.read_csv('all_sub_all_category.csv')

# sub_a = int(sys.argv[1]) - 1
# sub_b = int(sys.argv[2]) - 1

age_0_4 = []
age_5_9 = []
age_10_14 = []
age_15_19 = []
age_20_24 = []
age_25_44 = []
age_45_64 = []
age_65_69 = []
age_70_74 = []
age_75_79 = []
age_80_84 = []
age_85 = []
pharmacies = []
hospitaldist = []
hospitaltime = []
aged_Care_High_Care = []
aged_Care_Low_Care = []
kinder_Childcare = []
primary_Schools = []
secondary_Schools = []

age_0_4 = to_float(get_table('2012 ERP age 0-4, %', age_0_4))
age_5_9 = to_float(get_table('2012 ERP age 5-9, %', age_5_9))
age_10_14 = to_float(get_table('2012 ERP age 10-14, %', age_10_14))
age_15_19 = to_float(get_table('2012 ERP age 15-19, %', age_15_19))
age_20_24 = to_float(get_table('2012 ERP age 20-24, %', age_20_24))
age_25_44 = to_float(get_table('2012 ERP age 25-44, %', age_25_44))
age_45_64 = to_float(get_table('2012 ERP age 45-64, %', age_45_64))
age_65_69 = to_float(get_table('2012 ERP age 65-69, %', age_65_69))
age_70_74 = to_float(get_table('2012 ERP age 70-74, %', age_70_74))
age_75_79 = to_float(get_table('2012 ERP age 75-79, %', age_75_79))
age_80_84 = to_float(get_table('2012 ERP age 80-84, %', age_80_84))
age_85 = to_float(get_table('2012 ERP age 85+, %', age_85))
pharmacies = to_float(get_table('Pharmacies', pharmacies))
hospitaltime = to_float(get_table('Travel time to nearest public hospital', hospitaltime))
hospitaldist = to_float(get_table('Distance to nearest public hospital', hospitaldist))
aged_Care_High_Care = to_float(get_table('Aged Care (High Care)', aged_Care_High_Care))
aged_Care_Low_Care = to_float(get_table('Aged Care (Low Care)', aged_Care_Low_Care))
kinder_Childcare = to_float(get_table('Kinder and/or Childcare', kinder_Childcare))
primary_Schools = to_float(get_table('Primary Schools', primary_Schools))
secondary_Schools = to_float(get_table('Secondary Schools', secondary_Schools))

sub_id = all_sub_features['ID']
sub_id = sub_id.values.tolist()

id_features = []
id_features_2 = []
for i in range(34):
	id_features.append([sub_id[i], age_0_4[i], age_5_9[i], age_10_14[i], age_15_19[i], age_20_24[i], age_25_44[i],
	    age_45_64[i], age_65_69[i], age_70_74[i], age_75_79[i], age_80_84[i], age_85[i]])
	id_features_2.append([sub_id[i], pharmacies[i], hospitaltime[i], hospitaldist[i], aged_Care_Low_Care[i], 
		aged_Care_High_Care[i], kinder_Childcare[i], primary_Schools[i], secondary_Schools[i]])

# print (similarity_sub(id_features[sub_a][1:], id_features[sub_b][1:], 12))

matrix_value = []

# generate and output scores

def distance_metrix():
	scores = []
	for i in range(34):
	    score = []
	    for j in range(34):
	    	dist1 = sm.bhatta_distance(id_features[i][1:],id_features[j][1:],12)
	    	dist2 = sm.euclidean_distance(id_features_2[i][1:],id_features_2[j][1:])
	    	score.append((dist1+dist2)/2)
	    scores.append(score)
	return scores

# print(sm.bhatta_distance(id_features[2][1:],id_features[2][1:],12))
