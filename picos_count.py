# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:50:38 2015

@author: alumno
"""
import matplotlib.pyplot as plt

def countpeaks(vec,umbral):#,sep):
    cuenta = 0
    for i in range(1,len(vec)-1):
        if vec[i] > umbral and\
        vec[i] > vec[i-1] and vec[i] > vec[i+1]:
            cuenta += 1
    return cuenta
vecprueba = [1,1,1,2,2,2,3,1,0,5,5,4,3,2,3,2,2,2,1]
plt.figure(3)
plt.clf()
plt.plot(vecprueba,'*-')
print(countpeaks(vecprueba,1))


    
            