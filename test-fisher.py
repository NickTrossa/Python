# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:09:26 2015

@author: alumno

Test exacto de Fisher
"""
import numpy as np

n0 = 100
n1 = 2
pg = 0.01
pcg = 0.1

N = n0 + n1
tabla = np.array([[pcg*n0,n0*(1-pcg),n0],[pg*N-pcg*n0,n1-(pg*N-pcg*n0),n1],[pg*N,N*(1-pg),N]])
print(tabla)

chi2 = 0
for i in range(2):
    for j in range(2):
        pij = tabla[i,2]*tabla[j,2]
        chi2 += (tabla[i,j]*(1-pij/N**2))**2/(N*pij)

print(chi2)