#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import pandas as pd
import csv
import sys
import locale
from sklearn import preprocessing
from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
import similarity_measure as sm
import similarity_geography as sm_geo
import similarity_industry_diversity as sm_idus_diversity
import similarity_cultural_diversity as sm_cult_diversity
import similarity_population as sm_pop_diversity

def plot_population():
    similarities = sm_pop_diversity.distance_metrix()
    similarities = np.array(similarities)
    similarities = similarities.reshape(34, 34)
    sub_id =  list(range(1, 35))
    mds = manifold.MDS(n_components=2, max_iter=5000, eps=1e-9,
	                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit(similarities).embedding_

    all_sub_features = pd.read_csv('all_sub_all_category.csv')
    sub_name = all_sub_features['Name'].tolist()
    fig = plt.figure(1)
    for i in range(len(pos)):
        if(i == 7 or i == 8 or i == 10 or i == 30):
            plt.scatter(pos[i][0], pos[i][1], s=30, c='r')
        else:
	    plt.scatter(pos[i][0], pos[i][1], s=30, c='g')

    for i, txt in enumerate(sub_id):
        plt.annotate(txt, (pos[i][0], pos[i][1]))
    sub_id =  list(range(1, 35))
    plt.show()


def plot_cultural():
    similarities = sm_cult_diversity.distance_metrix()
    similarities = np.array(similarities)
    similarities = similarities.reshape(34, 34)
    sub_id =  list(range(1, 35))
    mds = manifold.MDS(n_components=2, max_iter=5000, eps=1e-9,
	                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit(similarities).embedding_

    all_sub_features = pd.read_csv('all_sub_all_category.csv')
    sub_name = all_sub_features['Name'].tolist()
    fig = plt.figure(1)
    for i in range(len(pos)):
        if pos[i][0] > -0.2 and pos[i][0] < 0.2 and pos[i][1] < 0.2 and pos[i][1] > 0:
            plt.scatter(pos[i][0], pos[i][1], s=30, c='b')
        if(i == 7 or i == 8 or i == 10 or i == 30):
            plt.scatter(pos[i][0], pos[i][1], s=30, c='r')
        else:
	    plt.scatter(pos[i][0], pos[i][1], s=30, c='g')

    for i, txt in enumerate(sub_id):
        plt.annotate(txt, (pos[i][0], pos[i][1]))
    sub_id =  list(range(1, 35))
    plt.show()



def plot_industry():
    similarities = sm_idus_diversity.distance_metrix()
    similarities = np.array(similarities)
    similarities = similarities.reshape(34, 34)
    sub_id =  list(range(1, 35))
    mds = manifold.MDS(n_components=2, max_iter=5000, eps=1e-9,
	                   dissimilarity="precomputed", n_jobs=1)
    pos = mds.fit(similarities).embedding_

    all_sub_features = pd.read_csv('all_sub_all_category.csv')
    sub_name = all_sub_features['Name'].tolist()
    fig = plt.figure(1)
### Idus
    for i in range(len(pos)):
        if pos[i][0] < 0 and pos[i][0] > -0.2 and pos[i][1] < -0.2 and pos[i][1] < 0:
            plt.scatter(pos[i][0], pos[i][1], s=30, c='b')
        if(i == 7 or i == 8 or i == 10 or i == 30):
	    plt.scatter(pos[i][0], pos[i][1], s=30, c='r')
        else:
	    plt.scatter(pos[i][0], pos[i][1], s=30, c='g')
    for i, txt in enumerate(sub_id):
        if(i == 7):
            plt.annotate(txt, (pos[i][0], pos[i][1]), xytext = (-50, 50), textcoords = 'offset points', ha = 'right', va = 'bottom',
	            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
		            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        elif(i == 8):
            plt.annotate(txt, (pos[i][0], pos[i][1]), xytext = (-20, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
	            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
		            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        elif(i == 10):
            plt.annotate(txt, (pos[i][0], pos[i][1]), xytext = (30, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
	            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
		            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        elif(i == 30):
            plt.annotate(txt, (pos[i][0], pos[i][1]), xytext = (50, 50), textcoords = 'offset points', ha = 'right', va = 'bottom',
	            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
		            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
        else:
            plt.annotate(txt, (pos[i][0], pos[i][1]))
    plt.show()



#similarities = sm_pop_diversity.distance_metrix()
plot_industry()
plot_cultural()
plot_population()
