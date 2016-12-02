# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:49:47 2015

@author: alumno
"""
import numpy as NP
from scipy import linalg as LA

A = NP.array([[-18,9],[-3,6]])
print(A)
e_vals, e_vecs = LA.eig(A)


print(e_vals)
print(e_vecs)