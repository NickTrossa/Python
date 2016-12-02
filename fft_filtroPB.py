# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:51:09 2015

@author: alumno

Filtro de señal
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import *

def filtro(data,fc,fs=1):
    """
    Filtra pasa bajos de la señal data
    Frecuencia de corte = fc
    """
    N = len(data)
    tf = np.fft.fft(data)
    fcc = fc/fs
    for i in range(round(fcc*N),int(N/2)):
        tf[i] = 0
        tf[N-i] = 0    
    return np.real(np.fft.ifft(tf))

def fun(t):
    f1 = 0.2
    f2 = 0.02
    return sin(2*np.pi*f1*t)+sin(2*np.pi*f2*t)

t = np.arange(100)
signal = fun(t)

plt.figure(3),plt.clf()
plt.plot(signal,'b-')
plt.plot(filtro(signal,0.201),'k+-')
plt.show()
"""
tau = 4.
f = 1/tau

T = 15.
N = 16

t = linspace(0,T,N)
def fun(t):
    return sin(2*pi*f*t) + sin(2*pi/16*t)
def fun2(t):
    return sin(2*pi/16*t)

# fft normal
F = fft(fun(t))
absF = absolute(F)**2*2/N

frec = arange(N)/T

figure(1),clf(),title('DFT')
plot(frec,absF,'*-')


## fft real
#rfft = np.fft.rfft(y)*2/len(y)
#rfft = np.absolute(rfft)**2
#frec = np.arange(len(rfft))/T

def filtro_pb(vec,fc):
    filtrada = vec
    N = len(vec)
    for i in range(round(fc*N),int(N/2)):
        filtrada[i] = 0
        filtrada[N-i] = 0
    return filtrada

fc = 0.2
fif = ifft(filtro_pb(F,fc))
fi = ifft(F)

figure(2),clf()
plot(t,fi,'r*',label='IDFT',ms=12)
plot(t,fun(t),'b-+',label='Señal')
plot(t,fif,'r--',label='filtro %.2f'%fc)

z = linspace(0,T,100)
plot(z,fun2(z),'k',label='Filtro teorico')
plot(z,fun(z),'k',label='Analog.')
legend()
'''
def fft_real(y,t):
    T = t[-1]-t[0]
    return frec, rfft    
frec, rfft = fft_real
'''
"""
