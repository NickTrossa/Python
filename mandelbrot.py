# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 05:00:02 2016

@author: alumno
"""
import numpy as np
import matplotlib.pyplot as plt
from time import time

N = 100 #Iteraciones por pixel
z = 0 #Condición inicial
lado = 300
xs = np.linspace(-2,2,lado)
ys = np.linspace(-1,1,lado)

escala = []

t0 = time()
ny = 0
for y in ys:
    ny += 1
    for x in xs:
        c = x + 1j * y
        n = 0
        z = 0
        while n < N:
            n += 1
            if np.absolute(z**2 + c) > 1e2:
                escala.append(n)
                break
            else:
                z = z**2 + c
        else:
            escala.append(N)
    if (ny-1)%10 == 0:
        te = (time()- t0)/ny
        print("Tiempo restante:",round(te*(lado-ny))," s")
            
X = np.array(escala).reshape(lado,lado)
plt.figure(1),plt.clf()
plt.colormaps()
plt.imshow(X)
plt.show()
"""
c = 1
N = 2
x0 = 1 + 1j
puntos = [x0]
n = 0
while n < N:
    n += 1
    puntos.append(puntos[-1]**2+c)

real = []
imag = []
for punto in puntos:
    real.append(punto.real)
    imag.append(punto.imag)
plt.figure(1),plt.clf()
plt.plot(real,imag,'o')
"""
