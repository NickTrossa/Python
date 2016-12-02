# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:43:20 2015

@author: alumno
"""
from matplotlib.pylab import *
from random import random

figure(1)
clf()
mu = 5
b = 1
def fun(x,mu,b):
    return exp(-abs(x-mu)/b)/2/b

def g1(x,mu,b):
    return b*log(2*x)+mu
def g2(x,mu,b):
    return -b*log(2*(1-x))+mu


N = 10000
y = []
for k in range(N):
    num = random()
    if num <= .5:
        y.append( g1(num,mu,b) )
    else:
        y.append( g2(num,mu,b) )

bines = arange(-1,12,.2)
hist(y,normed=True,bins=bines)


z = linspace(min(y),max(y),200)
plot(z,fun(z,mu,b),'r')