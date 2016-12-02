# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 23:13:51 2015

@author: alumno
"""
# Serie de Fibonacci
'''
serie = [1,1]
cant_elementos = 20
for numero in range(cant_elementos-2):
    serie.append(serie[numero] + serie[numero+1])
print serie
'''
########
'''
cant_elementos = 20
serie = ones(cant_elementos)
for numero in range(cant_elementos-2):
    serie[numero + 2] = serie[numero] + serie[numero + 1]
    
print serie
print "Mide " + str(len(serie))

cocientes = [serie[k+1]/serie[k] for k in range(cant_elementos-1)]
phi = (1+sqrt(5.0))/2 * ones(cant_elementos)

figure()
plot(cocientes,'*')
plot(phi)
xlabel("Elemento")
ylabel("Valor")
'''
########
import numpy as np
M = np.array([0,1,1,1]).reshape(2,2)
phi1 = (1+np.sqrt(5))/2
phi2 = (1-np.sqrt(5))/2
C = np.array([1,1,phi1,phi2]).reshape(2,2)
D = np.array([phi1,0,0,phi2]).reshape(2,2)
vec0 = np.array([[1],[1]])

n = int(input("Ingrese el número de elemento de la sucesión de Fibonacci que quiere conocer: "))
def elementofibo(n):
    vecn = np.dot(np.dot(C,np.dot(D**(n-1),np.linalg.inv(C))),vec0)
    return vecn[0]
numn = elementofibo(n)
print("El %s-ésimo elemento de la sucesión de Fibonacci es %s."%(n,numn))
    
