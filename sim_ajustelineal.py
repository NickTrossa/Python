# -*- coding: utf-8 -*-
"""
Ajuste lineal con errores gaussianos
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from random import gauss

N = 15
x = np.linspace(0,50,N)

# Armo la dispersion en y
y = np.array([])
errores = np.array([])
for i in range(N):
    if i < 10:
        errores = np.append(errores,.5)
        y = np.append(y,gauss(x[i]/3+10,errores[i]))
    else:
        errores = np.append(errores,.5)
        y = np.append(y,gauss(x[i]/3+10,errores[i]))



# Supongo mediciones no correlacionadas --> V prop. Id.
# El ajuste es lineal en x, pero puede ser lineal en theta
A = np.ones((N,2))
A[:,1] = x
Vi = np.diag(1/errores**2)

B = np.linalg.inv( np.dot(np.transpose(A),np.dot(Vi,A)))
theta = np.dot(np.dot(B, np.transpose(A)),np.dot(Vi,y))

#slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

# Coeficiente R2
fit = theta[0]+theta[1]*x
r2 = 1 - sum((y-fit)**2)/sum((y-np.mean(y))**2)
# Coeficiente Chi2
chi2 = np.dot(np.transpose(y-fit),np.dot(Vi,y-fit))/(N-2)

#%%
plt.figure(1)
plt.clf()
plt.grid()
plt.errorbar(x,y,fmt='o',yerr=errores)

z = np.linspace(x[0],x[-1],1000)
plt.plot(z,theta[0]+theta[1]*z,'r')
print("R^2 =",r2)
print("Chi^2 =",chi2)