# -*- coding: utf-8 -*-

# Programa para alinear el instrumental en la práctica del efecto fotoeléctrico usando un LockIn 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from math import *
#---------------------------------------------------------------
## Armo los puntos a plotear
t0 = time.time()
def generopuntos():
    t = -1
    while t < 11:
        t += 1
        yield t, time.time()-t0
generador = generopuntos()
#---------------------------------------------------------------
## Creo la figura con sus propiedades
#plt.figure(1)
plt.close('all')
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
plt.axis((0,14,0,14))
plt.grid()
plt.xlabel('t')
plt.ylabel('Tiempo de máquina')
plt.title('Animación')
#---------------------------------------------------------------
## Defino la función que va a crear los cuadros de la animación
xdata, ydata = [], []
def run(data):
    # update the data
    t,y = data
    xdata.append(t)
    ydata.append(y)
    # Ejes movibles
#    xmin, xmax = ax.get_xlim()
#    ymin, ymax = ax.get_ylim()
#    if t >= xmax:
#        ax.set_xlim(xmin, 2*xmax)
#        ax.figure.canvas.draw()
#    if y >= ymax:
#        ax.set_ylim(ymin, 2*ymax)
#        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,
#---------------------------------------------------------------
## LLamo a la función mágica que hace el trabajo
ani = animation.FuncAnimation(fig, run, generador, blit=True, interval=1000,
    repeat=False)
plt.show()
