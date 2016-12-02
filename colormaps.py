# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 05:38:33 2016

@author: alumno
"""

import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(0,10,101)
ys = xs
X = np.ones((100,100))
for i in range(100):
    for j in range(100):
        X[i,j] = xs[i]+ys[j]
plt.figure(1),plt.clf()
plt.colormaps()
plt.imshow(X)
plt.show()
