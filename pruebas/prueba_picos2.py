# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:37:30 2015

@author: alumno
"""
from matplotlib.pylab import *
# Busco maximos

puntos = array([1,1,1,2,3,4,5,4,3,2,1,1,2,2,3,3,4,4,5,5,6,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,8,9,10,11,11,11,10,9,8,7,6])
def countpeaks(vec,umbral):
    cuenta = 0
    lugares = []
    for i in range(1,len(vec)-4):
        if vec[i] > umbral and\
        vec[i] >= vec[i-1] and vec[i] > vec[i+1] and\
        vec[i] >= vec[i-3] and vec[i] > vec[i+3]: #Filtro los picos pequeños
            cuenta += 1
            lugares.append(i)
    return cuenta,array(lugares)

figure(4),clf()
a,b = countpeaks(puntos,1.5)
plot(puntos,'b+-')
plot(b,puntos[b],'ro')