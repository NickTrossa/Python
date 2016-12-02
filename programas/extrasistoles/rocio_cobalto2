# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:38:34 2015

@author: alumno
"""

import matplotlib.pyplot as plt
import numpy as np
from rocio_aux2 import filtro,calc_umbral_2,busco_minimos,saco_minimos,armo_secuencia
plt.close('all')
#%% Cargo datos y veo la señal

path = '/home/alumno/Downloads/Descargas/rocio/extrasistoles050915'
archivo = '/15'
y = -np.loadtxt(path + archivo +'.csv',delimiter=',',skiprows=2, usecols=[1])

plt.figure(1),plt.clf()
plt.plot(y,'o-')
print('Datos cargados como "y"')
#%% Defino el inicio y filtro
total = len(y)
inicio = 1320 # Posición del 1er dato a analizar (en tiempo)
prop = 0.05 #Criterio para determinar qué proporción del alto del pulso tiene que tener el pico para contarlo
bajada_umbral = 0.2 #Qué tan abajo respecto del medio de los pulsos está el umbral.
#sup = 2669
sup=59349 # Posición del último dato a analizar (en tiempo)
frec_filtro = 8./48 # No es necesario cambiarla a menos que deforme mucho la señal. En ese caso aumentar un par el numerador


inf = inicio

amporiginal = y[inf:sup]
amp = filtro(amporiginal,frec_filtro)

umbral = calc_umbral_2(amp,bajada_umbral)
mins = busco_minimos(amp,umbral,cp=0)
## Saco los minimos que estan fuera de lugar con el criterio del cociente
newmins = saco_minimos(mins)


fibs,duds,minslocs,maxlocs,analizados = armo_secuencia(amp,newmins,prop)

plt.figure(3),plt.clf()#,plt.xlabel('Tiempo (arb. un.)'),plt.ylabel('Amplitud')
plt.plot(-amp,'k+-',label='Señal filtrada')
plt.plot(-umbral,'k',label='Umbral dinámico')
plt.plot(-amporiginal,'+-',label='Señal')

plt.plot(newmins,-amp[newmins],'yo',ms=7,label='Picos minimos filtrados')
plt.plot(minslocs,-amp[minslocs],'go',ms=10,label='Minimos')
plt.plot(maxlocs,-amp[maxlocs],'bo',ms=10,label='Maximos')

top,bot = max(amp),min(amp)
plt.vlines(fibs,-bot*np.ones(len(fibs)),-top*np.ones(len(fibs)),'r',label='Fibrilaciones',lw=3)
plt.vlines(duds,-bot*np.ones(len(duds)),-top*np.ones(len(duds)),'g',label='Dudosos',lw=3)
#plt.legend(loc=3)

if len(fibs) > 1:
    plt.figure(4),plt.clf()
    plt.hist(fibs)
    plt.title(archivo)
    plt.savefig(path+archivo)
print('Fibrilaciones',len(fibs))
print('Dudosos',len(duds))

print('Fin')

"""
plt.figure(2)
plt.plot(amporiginal,'b+-',label='Original')
plt.plot(filtrada,'r*--',label='Filtrada')
plt.legend()


plt.plot(mins,amp[mins],'ko',ms=4,label='Picos minimos')

muestral = fibs
contador = 0
for i in range(len(fibs)-1):
    if fibs[i] == fibs[i+1]:
        muestral[i] += 3
        contador += 1
print('Contador de repetidos',contador)
"""
