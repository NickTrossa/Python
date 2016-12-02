# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:24:15 2014

@author: alumno
"""
import os
os.system('clear')
currentpath = os.getcwd()

execfile(currentpath + '/print_tablero.py')
execfile(currentpath + '/colocobarcosmp.py')
execfile(currentpath + '/disparar.py')

# execfile(currentpath + '/colocobarcos.py')

L=6
print "Nombre de los jugadores"
players = [raw_input("Jugador 1: "), raw_input("Jugador 2: ")]

letras = ['A','B','C','D','E','F','G','H','I','J',\
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print "Comienza la guerra. Es hora de distribuir los barcos: \
 un bote, un acorazado y un portaaviones."
 
############################
tableros = [[],[]]
mapas = [[],[]]
for k in range(2):
    players[k] = players[k][0].upper() + players[k][1:]
    print "Turno de " + players[k]
    raw_input("Presionar <enter> para continuar...")
    #print "Clean"
    os.system('clear')
    
    tableros[k] = colocobarcosmp(players[k],L)
    #tableros[k] = colocobarcos(L)
    #print "Clean"
    os.system('clear')
    print "Esta es tu flota, " + players[k] + ": "
    print_tablero(tableros[k])
    
    print " "
    raw_input("Presionar <enter> para continuar...")
    #print "Clean"
    os.system('clear')
    
    for x in range(L):
        mapas[k].append(["O"] * L)
#####################################


contador = [[0,0,0],[0,0,0]] # Mide la cantidad de barcos
num = 0
continua = True
while continua:
    turno = num % 2
    raw_input("Es el turno de " + players[turno] + " ...")
    #print "Clean"
    os.system('clear')
    continua = disparar(num,continua,L,tableros,mapas,contador,players)
    num += 1
    
raw_input("Presiona <enter> para finalizar.")