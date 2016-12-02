# -*- coding: utf-8 -*-
"""
Created on Mon May 25 02:06:17 2015

@author: alumno
"""

import matplotlib.pyplot as plt
plt.close('all')

t = range(-10,11)
x = [i-1 for i in t]
y = [i**2 for i in t]
z = [i**3 for i in t]
w = [i**2-10 for i in t]

fig = plt.figure()
fig.suptitle('Sub-gráficos',fontsize=14)

ax = plt.subplot(2,2,1)
ax.scatter(t,x)
ax.set_xticklabels([])
ax.set_yticklabels([])

ax = plt.subplot(2,2,2)
ax.plot(t,y)
ax.set_xticklabels([])
ax.set_yticklabels([])

ax = plt.subplot(2,2,3)
ax.plot(t,z)
ax.set_xticklabels([])
ax.set_yticklabels([])

ax = plt.subplot(2,2,4)
ax.plot(t,w)
ax.set_xticklabels([])
ax.set_yticklabels([])