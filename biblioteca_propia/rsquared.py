# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:18:05 2015

@author: alumno
"""

def rsquared(x,y,fit):
    """
    Función que calcula el coeficiente de determinación
    x son los datos de la variable independiente
    y son los datos de la variable dependiente
    fit son los valores obtenidos por el modelo
    """
    import numpy as np
    
    y_m = np.mean(y)
    SS_tot = sum((y-y_m)**2)
    #SS_reg = sum((fun(x)-y_m)**2)
    SS_res = sum((y-fit)**2)
    return 1-SS_res/SS_tot