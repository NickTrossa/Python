# -*- coding: utf-8 -*-
"""
Monte Carlo
"""
import numpy as np
import matplotlib.pyplot as plt

def montecarlo(f,fm,a,b,N):
    """
    f es la función de distribución que se desea simular
    fm es su máximo
    [a,b] es el intervalo donde la función está definida
    N es la cantidad de elementos que deseo generar con el método MC
    """
    from random import random
    from numpy import array
    x = []
    i = 0
    while i < N:
        u = a + (b-a)*random()
        if fm*random() <= f(u):
          x.append(u)
          i += 1
    return array(x)

"""
def f(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)

x = montecarlo(f,np.sqrt(2*np.pi),-10,10,1000)

#%%
y = np.linspace(-6,6,1000)
plt.figure(2)
plt.clf()
plt.hist(x,normed=True)
plt.plot(y,f(y),'r')
"""