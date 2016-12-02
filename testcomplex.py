# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:25:18 2015

@author: alumno
"""
from numpy import *
import matplotlib.pyplot as plt
"""
Grafico funciones complejas como parte imaginaria vs parte real
"""
a = linspace(0,2*pi,100)

circ = exp(1j*a)

c = 4
d = 1
elipse = d*cos(a) + 1j*c*sin(a)


elipse2 = ((c-d)/2*cos(2*a)+(c+d)/2)*exp(2j*a)

plt.clf()
plt.plot(circ.real,circ.imag)
plt.plot(elipse.real,elipse.imag,'k')
plt.plot(elipse2.real,elipse2.imag,'r')

plt.show()

