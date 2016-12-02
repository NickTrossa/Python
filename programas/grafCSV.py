import numpy as np
import matplotlib.pyplot as plt
print("-- Graficador de .csv ---")

directorio = input('¿Directorio? >> ')
cols = [int(a) for a in input('¿Columnas (ej:" >> 24" para la 3ra y 5ta)? >> ')]
skipr = int(input('Saltear filas ("0" si no hay que saltear): >> '))

x, y = np.loadtxt(directorio, delimiter=',', usecols=cols, unpack=True, skiprows=skipr)
plt.plot(x,y,'o-')
plt.show()
