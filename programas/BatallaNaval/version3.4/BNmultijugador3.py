#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
from random import random
"""
from disparar3 import disparar
from colocobarcosmp3 import colocobarcosmp
from colocobarcos import colocobarcos
from print_tablero import print_tablero
from dispararIA import dispararIA
"""
from auxiliar_bn import dispararIA, disparar, colocobarcos, colocobarcosmp, print_tablero

os.system('clear')
print("--> Batalla Naval 2.0 - Jedai Studios <--")

auto = False
if input('\nElige un modo de juego:\n\tUn jugador\t[1]\n\tDos jugadores\t[2]\n>> ') == '1':
    auto = True

if auto:
    print('Jugarás contra la máquina...')
    players = [input("Escribe tu nombre: "), "Terminator"]
else:
    print("Nombre de los jugadores")
    players = [input("Jugador 1: "), input("Jugador 2: ")]    


print("Comienza la guerra. Es hora de distribuir los barcos: \n\
un bote, un acorazado y un portaaviones.\n")

startblue = "\033[0;34m"
startred = "\033[0;31m"
endcolor = "\033[0;0m"
P = startred + 'P' + endcolor
A = startred + 'A' + endcolor
B = startred + 'B' + endcolor
X = startblue + 'X' + endcolor

L=6
letras = ['A','B','C','D','E','F','G','H','I','J',\
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
barcos = ['poortaviones','acorazado','bote']
longitudes = [5,3,1]
ref = [P,A,B]

variables = (L,barcos,longitudes,letras,P,A,B,X,ref)
############################
tableros = [[],[]]
mapas = [[],[]]
for k in range(2):
    if not auto or k == 0:
        players[k] = players[k][0].upper() + players[k][1:]
        print("Turno de " + players[k])
        input("Presionar <enter> para continuar...")
        
        if input('¿Distribuir la flota al azar? [s]/n') == 'n':
            tableros[k] = colocobarcosmp(players[k],variables)
        else:
            tableros[k] = colocobarcos(variables)
        os.system('clear')
        print("Esta es tu flota, " + players[k] + ": ")
        print_tablero(tableros[k])

        input("\nPresionar <enter> para continuar...")
        
        for x in range(L):
            mapas[k].append(["O"] * L)
    else:
        players[k] = players[k][0].upper() + players[k][1:]
        print("Turno de " + players[k])
        input("Presionar <enter> para continuar...")
        tableros[k] = colocobarcos(variables)

        os.system('clear')
        print("Se han dispuesto los barcos de " + players[k] + "...")
        #print_tablero(tableros[k])
 
        mapas[k] = tableros[0] # Para mostrar las partes de los barcos que fueron tocadas
#####################################


contador = [[0,0,0],[0,0,0]] # Mide la cantidad de barcos
num = 0
continua = True
while continua:
    turno = num % 2
    input("Es el turno de " + players[turno] + " (presionar <enter> para continuar) ...")
    
    if auto and turno == 1:
        continua = dispararIA(num,continua,L,tableros,mapas,contador,players,variables)
    else:
        continua = disparar(num,continua,tableros,mapas,contador,players,variables)
    num += 1
    
input("Presiona <enter> para finalizar.")



'''
print(inspect.getfile(inspect.currentframe())) # script filename (usually with path)
currentpath = os.getcwd()
with open(currentpath + '/print_tablero.py') as f:
    code = compile(f.read(), currentpath + '/print_tablero.py', 'exec')
    exec(code)
with open(currentpath + '/colocobarcosmp3.py') as f:
    code = compile(f.read(), currentpath + '/colocobarcosmp3.py', 'exec')
    exec(code)
with open(currentpath + '/disparar3.py') as f:
    code = compile(f.read(), currentpath + '/disparar.py', 'exec')
    exec(code)
'''
