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

sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1

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

sub_id = all_sub_features['ID']
sub_id = sub_id.values.tolist()


id_features = []
for i in range(34):
    id_features.append([sub_id[i], age_0_4[i], age_5_9[i], age_10_14[i], age_15_19[i], age_20_24[i], age_25_44[i],
	    age_45_64[i], age_65_69[i], age_70_74[i], age_75_79[i], age_80_84[i], age_85[i]])

#print similarity_sub(id_features[sub_a][1:], id_features[sub_b][1:], 12)

h1 = [2.0,2.0,5.0,1.0]
h2 = [2.0,2.0,5.0,1.0]
print sm.dis_to_sim(sm.bhatta_distance(h1, h2, 4))
