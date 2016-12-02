# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:19:45 2015

@author: alumno
"""

from random import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# Genero distribucion gaussiana a partir de distribucion uniforme
def fun(x,y,a):
    return np.sqrt(-2*a*np.log(x))*np.sin(2*np.pi*y)

a = 2
muestra = []
for i in range(10000):
    muestra.append(fun(random(),random(),a))

plt.figure(5),plt.clf()
hb = plt.hist(muestra,bins=25,normed=True)

x = np.linspace(hb[1][0],hb[1][-1],100)
plt.plot(x,norm.pdf(x,0,np.sqrt(a)),'r')
plt.show()
