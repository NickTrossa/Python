# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:18:30 2015

@author: alumno
"""
# Creo variables con ditintos nombres en un loop

N = 3
a = 0
for num in [str(i) for i in range(N)]:
    a += 1
    locals()['datos' + num] = a
print(datos0)    
print(datos1)
print(datos2)
