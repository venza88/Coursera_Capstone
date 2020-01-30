# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:53:30 2020

@author: Dragon
"""

import pandas as pd
import numpy as np

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

import folium # map rendering library

df=pd.read_csv("Toronto_GeoPostal.csv")
#print(len(df["Latitude"].mean())      )

