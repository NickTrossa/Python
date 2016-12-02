#!/home/alumno/anaconda/bin/python2.7
# -*- coding: utf-8 -*-

from math import e,sqrt,pi
from pylab import *

M = int(input("Ingrese cantidad de números para calcular sus factoriales: "))

# Funcion factorial
def fac(n):
	factorial = 1
	for i in range(1,n+1):
		factorial *= i
	return factorial

def stirling(n):
	return sqrt(2*pi*n)*e**(-n)*n**n

factoriales = [0]*M
stirlings = [0]*M
cocientes = [0]*M
for N in range(M):
    factoriales[N] = fac(N)
    stirlings[N] = stirling(N)
    cocientes[N] = stirlings[N]/factoriales[N]
	
plot(factoriales,'*',label='Factorial')
plot(stirlings,label='Aproximación de Stirling')
xlabel("Número")
grid(True)

figure()
plot(cocientes)
show()

'''
print("El factorial del número es: " + str(fac))
print("La aproximación de Stirling da: " + str(St))

print("La razón entre ambos valores es: " + str(fac/St))
'''
