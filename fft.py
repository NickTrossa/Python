# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:48:34 2015

@author: alumno
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

tau = 2.
f = 1/tau

#t0 = 0
T = 10.
N = 2048

t = np.linspace(0,T,N)
y = np.sin(2*pi*f*t) + np.sin(2*pi*2*f*t)

# fft normal
fft = np.fft.fft(y)*2/N
fft2 = np.absolute(fft)**2

frec = np.arange(N)/T

plt.figure(5)
plt.plot(frec,fft2,'*-')

# fft real
rfft = np.fft.rfft(y)*2/len(y)
rfft = np.absolute(rfft)**2
frec = np.arange(len(rfft))/T

plt.figure(6)
plt.plot(frec,rfft,'*-')
plt.show()

'''
def fft_real(y,t):
    T = t[-1]-t[0]
    return frec, rfft    
frec, rfft = fft_real
'''
