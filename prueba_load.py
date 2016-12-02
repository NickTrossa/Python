# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:17:28 2015

@author: alumno
"""
import os
os.chdir('/home/alumno/L5/cristales/dia2/')

from matplotlib.pylab import loadtxt,plot


datos = loadtxt('cal_corta1.csv', delimiter=",")

v = datos[:,2]
print(v)

plot(range(2000,16000,1000),v)