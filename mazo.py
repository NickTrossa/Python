#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-

from random import random

N = 10000
exitos = 0
M = 5 # Cartas de la mano
def tengopar(mano):
    for i in range(len(mano)-1):
        for j in range(i+1,len(mano)):
            if mano[i] == mano[j]:
                return True
                break
        else:
            continue
        break
    else:
        return False
        
for i in range(N):
    mazo = list(range(1,14))*4

    mano = []
    for i in range(M):
        posicion = int(random()*len(mazo))
        mano.append(mazo[posicion])
        mazo.pop(posicion)
    if tengopar(mano):
        exitos += 1
prob = exitos/N
print('La probabilidad estimada de sacar un par en una mano de póquer es %.5f.' %prob)

np = 1
M = 52
for i in range(5):
    np *= (1-3*i/(N-i))
print('La probabilidad exacta de sacar un par en una mano de póquer es %.5f.' %(1-np))



input('Enter para finalizar')
