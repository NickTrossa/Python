# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:14:09 2015

@author: alumno
"""
from random import random


T = 30
N = 5

def experimento(T,N):
    llegada = []
    for i in range(N):
        llegada.append(T*random())
    return min(llegada)

expected = 0
M = 10000
for i in range(M):
    expected += experimento(T,N)

print('Valor esperado: %.2f minutos'%(expected/M))
print('Valor esperado teórico: %.2f minutos'%(T/(N+1)))

