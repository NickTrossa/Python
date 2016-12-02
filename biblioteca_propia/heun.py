#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-

import numpy as np

def heun(y0,t0,tf,h,f):
    '''
    Algoritmo para resolver ecuaciones diferenciales ordinarias de 1er orden.
    y0 es el vector fila con las condiciones iniciales
    t0 es el tiempo inicial tal que f(t0)=y(0)
    h es el paso
    La ecuación para f puede ser vectorial (el output de f debe ser una fila).
    Las columnas del output son los vectores con las sol. de la EDO.
    '''
    t = np.arange(t0,tf,h)
    n = len(t)
    y = np.zeros((n,len(y0)))
    y[0,:] = np.array(y0)
    for i in range(n-1):
        y[i+1,:] = y[i,:] + h/2*( f(t[i],y[i]) + f(t[i]+h,y[i]+h*f(t[i],y[i])))
    return y,t