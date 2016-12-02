# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:12:22 2015

@author: alumno
"""

#import numpy as np

def printarray(mat,dig):
    """
    Muestra en la consola la matriz con 'dig' cifras significativas.
    """
    fil = mat.shape[0]
    col = mat.shape[1]
    fmt = '\%.%ie'%3
    print('[[',end=" ")
    for i in range(fil):
        for j in range(col):
            print('%.1e,'%mat[i,j],end=" ")
            if j==col-1 and i != fil-1:
                print(']\n[',end= " ")
            elif j==col-1 and i == fil-1:
                print(']]\n',end= " ")