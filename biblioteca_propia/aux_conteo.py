# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:41:00 2015

@author: alumno
"""

import numpy as np

def countpeaks(vec,umbral):
    cuenta = 0
    for i in range(1,len(vec)-1):
        if vec[i] > umbral and\
        vec[i] > vec[i-1] and vec[i] > vec[i+1]:
            cuenta += 1
    return cuenta

def bose_einstein(x,mu):
    return mu**x/(1+mu)**(1+x)