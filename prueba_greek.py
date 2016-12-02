# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:32:56 2015

@author: alumno
"""

import matplotlib.pylab as plt

plt.close(True)

f, axarr = plt.subplots(2, sharex=True)

axarr[0].plot([1,2,3])
axarr[1].plot([3,4,5])
plt.xlabel('wavelength $5000 \AA \lambda \alpha$')
plt.show()

'''
x = range(5)
y = range(3,9)
for xd,yd in zip(x,y):
    print(xd,yd)
'''
