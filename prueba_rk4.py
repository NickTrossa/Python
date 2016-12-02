# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:13:54 2015

@author: alumno
"""

from biblioteca_propia.rk4 import rk4
import matplotlib.pyplot as plt
import numpy as np

def fun(t,y):
    a = 0.5
    b = 5
    v0 = 1
    w = 1
    return np.array([(v0*np.cos(w*t) - b*y)/a])

def prueba(t,y):
    a = 1
    return np.array([-a*y])

def sol(t):
    return np.exp(-t)
    
pr,ti = rk4(np.array([0]),0,20,0.2,fun)

plt.figure(1),plt.clf()

plt.plot(ti,pr,'r--')
plt.plot(ti[:-1], np.diff(pr[:,0]), 'go')
plt.show()
