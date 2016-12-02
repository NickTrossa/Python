# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:26:01 2015

@author: alumno
"""
# Resuelve un sistema lineal de ecuaciones
from matplotlib.pylab import *

v1=-18
v2=7
v3=20
r1=5
r2=8
r3=7

b = array([v1-v2,v1+v3])
a = array([[-r1, -r2-r1],[-r1-r3,-r1]])

i=solve(a,b)
print(i)
