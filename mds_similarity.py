
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

similarities = sm_geo.init()
similarities = euclidean_distances(similarities)
print similarities
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9,
	                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_
fig = plt.figure(1)
plt.scatter(pos[:, 0], pos[:, 1], s=30, c='g')
sub_id =  list(range(1, 35))
pos = pos.tolist()
print pos
for i, txt in enumerate(sub_id):
    plt.annotate(txt, (pos[i][0], pos[i][1]))
plt.show()
'''
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(np.float)
print X_true
X_true = X_true.reshape((n_samples, 2))
print X_true
# Center the data
X_true -= X_true.mean()
similarities = euclidean_distances(X_true)

print similarities
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
	                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_
clf = PCA(n_components=2)
X_true = clf.fit_transform(X_true)


fig = plt.figure(1)
ax = plt.axes([0., 0., 1., 1.])
plt.scatter(X_true[:, 0], X_true[:, 1], c='r', s=20)
plt.scatter(pos[:, 0], pos[:, 1], s=20, c='g')

plt.show()
'''


