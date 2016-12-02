# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:48:15 2014

@author: alumno
"""
# Colocar los barcos en modo multijugador

def colocobarcosmp(p,L):
    import os
    startred = "\033[0;31m"
    endcolor = "\033[0;0m"
    P = startred + 'P' + endcolor
    A = startred + 'A' + endcolor
    B = startred + 'B' + endcolor
    
    letras = ['A','B','C','D','E','F','G','H','I','J',\
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # Tablero
    tablero = []
    for x in range(L):
      tablero.append(["O"] * L)    
    
    print "Hola %s, debes elegir la ubicación de tus barcos. Este es el mapa táctico:"%(p)
    print_tablero(tablero)
    
    barcos = ['poortaviones','acorazado','bote']
    ref = [P,A,B]
    longitudes = [5,3,1]
    
    for k in range(len(barcos)):
        os.system('clear')
        print "Capitán %s, es hora de ubicar el %s. Ocupa %s casilleros." %(p,barcos[k], longitudes[k])

        print_tablero(tablero)
        if longitudes[k] != 1:
            vh = raw_input("Primero debes elegir si es vertical (v) u horizontal (h): ")
            while vh != 'v' and vh != 'h':
                vh = raw_input("¡Ups! Prueba de nuevo. Elige vertical (v) u horizontal (h): ")    
        else:
            vh = 'v'
        origen = raw_input("Elige la coordenada de origen (ej.: a2). ¡Ten en cuenta que debe entrar en el mapa!: ")
        incorrecto = True
        while incorrecto: 
            if len(origen) != 2 or origen[0].isalpha() == False or origen[1].isdigit() == False:
                origen = raw_input("¡Ups! Prueba de nuevo: ")
            else:
                origen = [letras.index(origen[0].upper()), int(origen[1]) - 1]
                if (vh == 'v' and (origen[0] > L-longitudes[k] or origen[1] > L-1)) \
                or (vh == 'h' and (origen[0] > L-1 or origen[1] > L-longitudes[k])):
                    origen = raw_input("¡Ups! Prueba de nuevo: ")
                else:
                    incorrecto = False

        for place in range(longitudes[k]):
            if vh == 'v':
                tablero[origen[0]+place][origen[1]] = ref[k]
            else:
                tablero[origen[0]][origen[1]+place] = ref[k]
    return tablero