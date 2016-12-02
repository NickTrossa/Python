# -*- coding: utf-8 -*-
"""
Prueba de métodos de integración
"""
from nicktrossa.heun import heun
from nicktrossa.euler import euler
import nicktrossa.rk4
from matplotlib.pylab import *

close('all')
def prueba(t,X):
    return array([X[0]])
t0 = 0
tf = 10

# Solución teórica
t1 = linspace(0,tf,1000)
teo = exp(t1)

'''
pasos = [0.001,0.01,0.1,1]
for h in pasos:
'''
h=0.1
figure()
title('Paso %f'%h)
# Euler
X,t = euler([1],t0,tf,h,prueba)
plot(t,X[:,0],'x',ms=10,label='Euler')
# Heun
X,t = heun([1],t0,tf,h,prueba)
plot(t,X[:,0],'o',ms=10,label='Heun')
#Runge-Kutta 4
X,t = nicktrossa.rk4.rk4([1],t0,tf,0.5,prueba)
plot(t,X[:,0],'+',ms=10,label='rk4')

plot(t1,teo,label='Teórica')
legend(loc=2)
draw()
