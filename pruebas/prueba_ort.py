# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:33:06 2015

@author: alumno
"""

from matplotlib.pylab import *

x = array([[0,0],[2,1]])

def ort(y0,y1):
    v = y1-y0
    vec = np.array([v[1],-v[0]])#/sqrt(v[0]**2+v[1]**2)
    yout = y1 + vec
    return yout

y = array([ x[1,:], ort(x[0,:],x[1,:]) ])
figure(6),clf()
show()
plot(x[:,0],x[:,1],'bo-',ms=12)
plot(y[:,0],y[:,1],'ro-',ms=12)
axis((-3,3,-3,3))
input('Presione una tecla para finalizar')
