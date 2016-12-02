# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 00:58:15 2014

@author: alumno
"""
import os
os.system('clear')
currentpath = os.getcwd()
execfile(currentpath + '/colocobarcos.py')
execfile(currentpath + '/print_tablero.py')

# Defino variables
L=6
turnos = 20
letras = ['A','B','C','D','E','F','G','H','I','J',\
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
startred = "\033[0;31m"
startblue = "\033[0;34m"
endcolor = "\033[0;0m"
P = startred + 'P' + endcolor
A = startred + 'A' + endcolor
B = startred + 'B' + endcolor
#D = startred + 'D' + endcolor # Barco adicional
#C = startred + 'C' + endcolor
#T = startred + 'T' + endcolor

X = startblue + 'X' + endcolor

barcos = ['poortaviones','acorazado','bote']
ref = [P,A,B]
longitudes = [5,3,1]

variables = [L,turnos,letras,startred,startblue,endcolor, \
barcos,ref,longitudes]

# Armo el tablero y lo muestro
te = colocobarcos(variables)
#print_tablero(te)
# Tablero
tablero = []
for x in range(L):
  tablero.append(["O"] * L)

name = raw_input("Escribe tu nombre, comandante: ")
name = name[0].upper() + name[1:]
print "%s, hemos avistado barcos enemigos. ¡Debemos hundirlos!"%(name)
raw_input("Presiona <enter> para continuar.")
os.system('clear')
print "Aquí tenemos el mapa táctico:"
print_tablero(tablero)
print 'Tienes ' + str(turnos) + ' balas para hundir los barcos.'
print ' '
raw_input("Si estás listo para comenzar el ataque presiona <enter>.")

CB = len(barcos)
contador = [0]*CB

for turn in range(turnos):
    # Se efectua el disparo
    disparo  = raw_input("Apunta a una coordenada: ")
    while len(disparo) != 2:
        disparo  = raw_input("¡Ups! Prueba de nuevo: ")
    
    adivina_fila = letras.index(disparo[0].upper()) + 1
    adivina_columna = int(disparo[1])
    disparo = [adivina_fila - 1, adivina_columna - 1]
    
    os.system('clear')
    # Veo que sucedio con el disparo
    # Veo que haya caido adentro y que no haya disparado ahi antes
    if (disparo[0] < 0 or disparo[0] > L-1) or (disparo[1] < 0 or disparo[1] > L-1):
        print "¡Uy!, eso ni siquiera esta en el océano."
        
    elif tablero[disparo[0]][disparo[1]] == X:
        print "Ya apuntaste a esa coordenada."
    elif tablero[disparo[0]][disparo[1]] != "O": # Tampoco X, pero se cumple
        print "Ya tocaste un barco allí."
    elif te[disparo[0]][disparo[1]] != "O":
        for barco in range(len(barcos)):
            if te[disparo[0]][disparo[1]] == ref[barco]:
                contador[barco] += 1
                tablero[disparo[0]][disparo[1]] = ref[barco]
                if contador[barco] < longitudes[barco]:
                    print "Tocaste su " + barcos[barco] + "."
                else:
                    print "¡Hundiste su " + barcos[barco] + "!"
    else:
        print "No tocaste mis barcos, %s." %(name)
        tablero[disparo[0]][disparo[1]] = X
    
    print_tablero(tablero)
    if sum(contador) == sum(longitudes):
        print "¡Has ganado %s!" %(name)
        break
    if turnos-turn-1 > 1:
        print "Te quedan " + str(turnos-turn-1) + " balas."
    elif turnos-turn-1 == 1:
        print "¡Te queda una última oportunidad!."
    else:
        print "Ya no te quedan balas, %s. Comenzaremos la retirada." %(name)
        raw_input("Presiona <enter> para ver la posición de los barcos enemigos.")
        print_tablero(te)
        print "Juego terminado"

print " "
raw_input("Presiona <enter> para finalizar.")

# Agregar balas si toca un barco en situación crítica