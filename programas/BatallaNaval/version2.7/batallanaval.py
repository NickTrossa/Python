# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 19:18:16 2014

@author: alumno
"""
import random

# Armo el tablero y lo muestro
tablero = []

for x in range(5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print " ".join(fila)

print "Juguemos a la batalla naval!"
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_columna = columna_aleatoria(tablero)
#print 'El barco esta en fila %s y columna %s.' %(barco_fila,barco_columna)

#¡De acá en adelante todo debería ir en tu ciclo for!
#¡Asegurate de indentar!
turnos = 4
for turn in range(turnos):
    if turn == 0:
        print 'Tienes ' + str(turnos) + ' balas para hundir el barco.'
    adivina_fila = input("Adivina fila: ")
    adivina_columna = input("Adivina columna: ")
    if adivina_fila == barco_fila + 1 and adivina_columna == barco_columna + 1:
        print "Felicitaciones! Hundiste mi barco!"
        break
    else:
        if (adivina_fila < 1 or adivina_fila > 5) or (adivina_columna < 1     or adivina_columna > 5):
            print "Huy, eso ni siquiera esta en el oceano."
        elif(tablero[adivina_fila - 1][adivina_columna - 1] == "X"):
            print "Ya apuntaste a esa coordenada."
        elif adivina_fila == '' or adivina_columna == '':
            print "Debes escribir algo!"
        else:
  	        print "No tocaste mi barco, ¡soquete!"
  	        tablero[adivina_fila - 1][adivina_columna - 1] = "X"
    if turn == turnos-1:
        print "GAME OVER LULA"
        

  # ¡Mostrá (turno + 1) acá!
    if turn < turnos-1:
        print 'Te quedan ' + str(turnos-turn-1) + ' chances de acertar.'
        print_tablero(tablero)
    else:
        print "Ya no te quedan disparos. Mira donde estaba el barco:"
        tablero[barco_fila][barco_columna] = "@"
        print_tablero(tablero)
