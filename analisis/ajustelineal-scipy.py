# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:08:58 2015

@author: alumno
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.2,2,2.8,4.4,5.6,6.1])

plt.figure()
plt.scatter(x,y,label='Datos')
plt.xlabel('x')
plt.ylabel('y')

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

xr = np.linspace(0,6,100)
yr = slope*xr + intercept
plt.plot(xr,yr,'r',label='Ajuste lineal')
plt.legend(loc=2)
plt.show()

print("r-squared:", r_value**2)
