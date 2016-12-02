# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:36:17 2016

@author: alumno
"""

import matplotlib.pyplot as plt
import numpy as np

angulos = np.linspace(0.01,2*np.pi-0.002,100)

p = 1
e = [0,0.5,1,2]

def radio(theta):
    return p/(1+e*np.cos(theta))

plt.figure(1), plt.clf()
for e in e:
    x = []
    y = []
    for th in angulos:
        x.append(radio(th)*np.cos(th))
        y.append(radio(th)*np.sin(th))
    plt.plot(x,y,label='e = %.2f'%e)
plt.legend(loc=0)