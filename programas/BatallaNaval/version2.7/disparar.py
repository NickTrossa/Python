# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 18:13:54 2014

@author: alumno
"""

def disparar(num,continua,L,tableros,mapas,contador,players):
    import os
    turno = num % 2
    te = tableros[(num+1) % 2]
    tablero = mapas[turno]
        
    
    # Defino lo necsario para que haya color
    startred = "\033[0;31m"
    startblue = "\033[0;34m"
    endcolor = "\033[0;0m"
    P = startred + 'P' + endcolor
    A = startred + 'A' + endcolor
    B = startred + 'B' + endcolor
    X = startblue + 'X' + endcolor
    
    letras = ['A','B','C','D','E','F','G','H','I','J',\
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    
    print "¡Es tu turno de disparar al enemigo! Este es tu mapa:"
    print_tablero(mapas[turno])
    # Se efectua el disparo
    disparo  = raw_input("Apunta a una coordenada: ")
    
    incorrecto = True
    while incorrecto: 
        if len(disparo) != 2 or disparo[0].isalpha() == False or disparo[1].isdigit() == False:
            disparo  = raw_input("¡Ups! Prueba de nuevo: ")
        else:
            incorrecto = False
    adivina_fila = letras.index(disparo[0].upper()) + 1
    adivina_columna = int(disparo[1])
    disparo = [adivina_fila - 1, adivina_columna - 1]

    #print "Clean"
    os.system('clear')


    # Veo que sucedio con el disparo
    barcos = ['poortaviones','acorazado','bote']
    ref = [P,A,B]
    longitudes = [5,3,1]
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
                contador[turno][barco] += 1
                tablero[disparo[0]][disparo[1]] = ref[barco]
                if contador[turno][barco] < longitudes[barco]:
                    print "Tocaste su " + barcos[barco] + "."
                else:
                    print "¡Hundiste su " + barcos[barco] + "!"
    else:
        print "No tocaste sus barcos, %s." %(players[turno])
        tablero[disparo[0]][disparo[1]] = X
    
    print_tablero(tablero)
    if sum(contador[turno]) == sum(longitudes):
        print "¡Ganaste %s!" %(players[turno])
        continua = False
    return continua