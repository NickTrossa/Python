# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:03:32 2015

@author: alumno

Minimizacion
"""
import numpy as np
from scipy.optimize import minimize
from time import time

def funcion(x):
    return x[0]**2+x[1]**2+2
def fun_der(x):
    return np.array([2*x[0],2*x[1]])
def hes(x):
    return 2*np.ones((2,2))

x0 = np.array([10,117])
t0 = time()

res = minimize(funcion, x0, method='nelder-mead',\
options={'disp': True})#'xtol': 1e-8, 
print(res.x)

res = minimize(funcion, x0, method='BFGS', jac=fun_der,\
options={'disp': True})
print(res.x)


res = minimize(funcion, x0, method='Newton-CG',\
jac=fun_der, hess=hes,\
options={'disp': True})#'xtol': 1e-8, 
print(res.x)


print('Tiempo: %.2f ms'%(1000*(time()-t0)))