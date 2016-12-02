# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:14:04 2015

@author: alumno

Ajuste cuadrático
"""
def ajustecuadratico(x,y,errores):
    """
    Ajusta los datos con una parábola a2*x^2+a1*x+a0 en el sentido de max verosimilitud
    errores es un array con las desviaciones estándar de los valores y
    x es un array con los valores independientes (sin error)
    y es un array con los datos medidos que se desea ajustar
    ---
    Devuelve: a0,a1,a2,r2,chi2,pcov
    pcov es la matriz de covarianza de a0,a1,a2
    """
    import numpy as np
    # Supongo mediciones no correlacionadas --> V prop. Id.
    # El ajuste es lineal en x, pero puede ser lineal en theta
    N = len(x)
    A = np.ones((N,3))
    A[:,1] = x
    A[:,2] = x**2
    Vi = np.diag(1/errores**2)
    
    def dotmat(matrices):
        N = len(matrices)
        M = np.dot(matrices[-2],matrices[-1])
        for i in range(N-2):
            M = np.dot(matrices[N-3-i],M)
        return M
    pcov = np.linalg.inv(dotmat([np.transpose(A),Vi,A]))
    theta = dotmat([pcov, np.transpose(A),Vi,y])
    a0 = theta[0]
    a1 = theta[1]
    a2 = theta[2]
    
    # Coeficiente R2
    fit = theta[0]+theta[1]*x+theta[2]*x**2
    r2 = 1 - sum((y-fit)**2)/sum((y-np.mean(y))**2)
    # Coeficiente Chi2
    chi2 = dotmat([np.transpose(y-fit),Vi,y-fit])/(N-3)
    return a0,a1,a2,r2,chi2,pcov
"""
EJEMPLO
import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.clf()
plt.grid()

x = np.array([-0.6,-0.2,0.2,0.6])
y = np.array([5,3,5,8])+2
errores = np.array([1,1,1,1])/2
plt.errorbar(x,y,fmt='o',yerr=errores)

a0,a1,a2,r2,chi2,pcov = ajustecuadratico(x,y,errores)


z = np.linspace(x[0]-(x[1]-x[0])/10,x[-1]+(x[1]-x[0])/10,1000)

def fit(y):
    return a0+a1*y+a2*y**2
estimacion = np.dot(np.transpose(y-fit(x)),y-fit(x))/(len(y)-3)

plt.plot(z,fit(z),'r')
print("R^2 =",r2)
print("Chi^2 =",chi2)
print(a0,a1,a2)
plt.show()
"""
