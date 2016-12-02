#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-

import numpy as np
from nicktrossa.euler import euler
from nicktrossa.animacion3D import animacion3D
'''
def campovector(t,X):
    return np.array([10*(X[1]-X[0]), 28*X[0]-X[1]-X[0]*X[2], X[0]*X[1]-8*X[2]/3])

X,t = euler([-1, -1, -1],0,50,0.01,campovector)
'''
animacion3D(X[:,0],X[:,1],X[:,2],title='Atractor de Lorenz',save=False)
