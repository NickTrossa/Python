# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:28:41 2015

@author: alumno

Auto-correlación
"""

from matplotlib.pylab import *
import numpy as np

t = np.linspace(0,10,1000)
tau = 0.5

y = np.sin(2*np.pi/tau*t)
plt.plot(t,y)

# Auto-correlación
aut = np.correlate(y,y,mode='same')

plt.figure(3)
plt.clf()
plt.plot(aut)
plt.show()
