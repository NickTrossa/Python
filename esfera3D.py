# -*- coding: utf-8 -*-
"""
Esfera al azar
"""
import numpy as np
from random import random
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

N = 10000
def generopunto():
    r = random()
    th = random()*np.pi
    ph = random()*2*np.pi
    x = r*np.sin(th)*np.cos(ph)
    y = r*np.sin(th)*np.sin(ph)
    z = r*np.cos(th) 
    return np.array([x,y,z])

puntos = []
for i in range(N):
    puntos.append(generopunto())
puntos = np.array(puntos)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(puntos[:,0], puntos[:,1], puntos[:,2],'o')#, label='')
ax.set_title('Esfera 3D')
#ax.view_init(azim=225,elev=None)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#ax.legend(loc=3)
plt.draw()
plt.show()
