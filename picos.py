# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:59:39 2015

@author: alumno
"""

# Encontrar picos

from numpy import *
import matplotlib.pyplot as plt

I = linspace(0,10*2*pi,1000)
F = sin(I)

maximos = array([])
abscisas = array([])
for point in range(1,len(F)-1):
    if F[point] > F[point-1] and F[point] > F[point+1]:
        maximos = append(maximos, F[point])
        abscisas = append(abscisas, I[point])

##########
plt.clf()
plt.figure(1)

plt.plot(I,F)

plt.plot(abscisas, maximos,'*', ms = 15)
plt.grid('on')
plt.show()
