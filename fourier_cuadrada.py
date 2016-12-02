# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:31:17 2015

@author: alumno
"""

import matplotlib.pyplot as plt
import numpy as np

N = 1000
t = np.linspace(0,4*np.pi,N)
def term(n,t):
    A = 1
    w = 1
    return 4*A/n/np.pi*np.sin(n*w*t)

y = np.zeros(N)
for i in range(80):
    if i % 2 != 0:
        y += term(i,t)

plt.figure(7),plt.clf()
plt.plot(t/np.pi, y,'r')
plt.show()
