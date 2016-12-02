# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:21:06 2015

@author: alumno
"""

from matplotlib.pylab import *

def fun(x,n):
    return sin(n**2*x)/n**2

x = linspace(0,1,100000)
y = zeros_like(x)

for i in range(100):
    y += fun(x,i+1)

figure(5),clf()
plot(x,y,'b-')