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
import similarity_diversity as sim_div
import similarity_land_use as sim_land


sub_a = int(sys.argv[1]) - 1
sub_b = int(sys.argv[2]) - 1

print (sim_land.similarity_land_use(sub_a, sub_b) + sim_div.similarity_diversity(sub_a, sub_b))/2




