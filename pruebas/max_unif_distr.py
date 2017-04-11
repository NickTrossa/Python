import numpy as np
import matplotlib.pyplot as plt
from random import random
"""
Simulación de N mediciones con distribucion uniforme entre 0 y 1
Quiero saber la distribucion de la variable aleatoria y = max{x},
el modelo dice que es N*u**(N-1)
"""
# Experimentos
M = 10000
# Cantidad de datos por experimento
N = 10

# Maximos
y = []
for i in range(M):
    maximo = 0
    for j in range(N):
        x = random()
        if x > maximo:
            maximo = x
    y.append(maximo)

plt.figure()
plt.hist(y,normed=True)

u = np.linspace(0,1,100)
plt.plot(u,N*u**(N-1))

plt.show()
