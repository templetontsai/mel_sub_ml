
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

similarities = sm_idus_diversity.distance_metrix()
#similarities = sm_cult_diversity.distance_metrix()
similarities = np.array(similarities)
similarities = similarities.reshape(34, 34)
#np.savetxt("industry_diversity_distance_metrix.csv", similarities, delimiter=",")
#np.savetxt("cultral_diversity_distance_metrix.csv", similarities, delimiter=",")
#print similarities
#similarities = sm_geo.init()
#similarities = euclidean_distances(similarities)
mds = manifold.MDS(n_components=2, max_iter=5000, eps=1e-9,
	                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

all_sub_features = pd.read_csv('all_sub_all_category.csv')
sub_name = all_sub_features['Name'].tolist()
fig = plt.figure(1)
plt.scatter(pos[:, 0], pos[:, 1], s=30, c='g')
sub_id =  list(range(1, 35))
pos = pos.tolist()
print pos
'''
for i, txt in enumerate(sub_name):
    plt.annotate(txt, (pos[i][0], pos[i][1]), xytext = (-20, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
	            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
		            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
'''
for i, txt in enumerate(sub_id):
    plt.annotate(txt, (pos[i][0], pos[i][1]))
plt.show()
