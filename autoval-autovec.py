# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:55:22 2016

@author: nicolas
"""

import numpy as np
from numpy import linalg as la

A = np.array([[0,1],[4,0]])
autoval, autovec = la.eig(A)
c = autovec
print(np.dot(c,np.dot(np.diag(autoval),la.inv(c) ) ) )
#la.inv()
#np.transpose()
#np.array()
#np.array([1,2])
