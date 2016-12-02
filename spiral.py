# -*- coding: utf-8 -*-
"""
prueba selector
"""

from matplotlib.pylab import *
from mpl_toolkits.mplot3d import Axes3D

close('all')

t = linspace(0,50,1000)
th = t
r = th

x = r*cos(th)
y = r*sin(th)
z = th

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)

figure()
ax=subplot(1,2,1)
ax.plot(x,y)

ang = pi/2-0.01
dots = []
dots_z = []
for i in range(1000-1):
    if (arctan(y[i]/x[i])-ang<=0 and arctan(y[i+1]/x[i+1])-ang>=0):
        dots.append(sign(x[i])*sqrt(y[i]**2+x[i]**2))
        dots_z.append(z[i])

ax = subplot(1,2,2)
ax.plot(dots,dots_z,'o',ms=12)

#or (arctan(y[i]/x[i])-ang>=0 and arctan(y[i+1]/x[i+1])-ang<=0):