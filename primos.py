# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:18:14 2015

@author: alumno
"""
from time import time
from math import sqrt
print("Algoritmo tradicional")
t0 = time()
def primos(n):
    lista=[]
    for i in range (1,n+1,2):
        for k in range(3,int(sqrt(i)),2):
            if i%k==0:
                break
        else:
            lista.append(i)
    return lista
res = primos(int(1e6))
print("Tiempo:", time()-t0)
print(*res)

from fractions import gcd
print("Formula recursiva de Rowland para obtener primos")

t0 = time()
primos = [7]
serie = [7]
primos = [7]
for i in range(100000):
    a = serie[-1]
    serie.append(a + gcd(i,a))
    primo = serie[-1]-serie[-2]
    if primo != 1:
        primos.append(primo)
print("Tiempo:", time()-t0)
print(*restas)
