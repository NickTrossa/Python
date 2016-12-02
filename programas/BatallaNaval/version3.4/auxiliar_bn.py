# -*- coding: utf-8 -*-

import os, inspect, pygame
from random import random, randint

def print_tablero(tablero):
    # Dibuja el tablero agregando el número de fila y columna a los costados
    L = len(tablero)
    letras = ['A','B','C','D','E','F','G','H','I','J',\
    'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    startbold = "\033[1m"
    endcolor = "\033[0;0m"
    # Armo la tira 1 2 --- L
    col = []
    for i in range(1,L+1):
        col.append(str(i))
    i=0
    for fila in tablero:
        i += 1
        if i == 1:
            print(startbold + "  " + " ".join(col) + endcolor)
        print(startbold + letras[i-1] + endcolor + ' ' + " ".join(fila))
    print("")
    '''
    startred = "\033[0;31m"
    startblue = "\033[0;34m"
    P = startred + 'P' + endcolor
    A = startred + 'A' + endcolor
    B = startred + 'B' + endcolor
    X = startblue + 'X' + endcolor
    print("Referencias:")
    print(X + ": Agua.")
    print(P + ": " + startbold + "portaaviones" + endcolor + ". Mide 5 cuadraditos.")
    print(A + ": " + startbold + "acorazado "+ endcolor + ". Mide 3 cuadraditos.")
    print(B + ": " + startbold + "bote"+ endcolor + ". Mide 1 cuadradito.")
    print(" ")
    '''
############################################################################
def dispararIA(num,continua,L,tableros,mapas,contador,players,variables):
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))# script directory
    pygame.mixer.init()
    pygame.mixer.music.load(path + "/bomb-04.wav")

    #turno = num % 2
    turno = 1
    #te = tableros[(num+1) % 2]
    tablero = mapas[turno]
    os.system('clear')
    L,barcos,longitudes,letras,P,A,B,X,ref = variables

    elem = X
    while elem == X:
        disparo = [int(random()*L), int(random()*L)]
        elem = tablero[disparo[0]][disparo[1]]

    # Veo que sucedio con el disparo
    # Veo que haya caido adentro y que no haya disparado ahi antes    
    if tablero[disparo[0]][disparo[1]] != "O":
        for barco in range(len(barcos)):
            if tablero[disparo[0]][disparo[1]] == ref[barco]:
                contador[turno][barco] += 1
                tablero[disparo[0]][disparo[1]] = X
                if contador[turno][barco] < longitudes[barco]:
                    print("Tocaron tu " + barcos[barco] + ".")
                    pygame.mixer.music.play()##
                else:
                    print("¡Hundieron tu " + barcos[barco] + "!")
                    pygame.mixer.music.play()##
    else:
        print("No tocaron tus barcos, %s." %(players[0]))
        tablero[disparo[0]][disparo[1]] = X
    
    print_tablero(tablero)
    if sum(contador[turno]) == sum(longitudes):
        print("¡Ganaste %s!" %(players[turno]))
        continua = False
    return continua
############################################################################
def disparar(num,continua,tableros,mapas,contador,players,variables):
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))# script directory
    pygame.mixer.init()
    pygame.mixer.music.load(path + "/bomb-04.wav")

    turno = num % 2
    te = tableros[(num+1) % 2]
    tablero = mapas[turno]
    
    L,barcos,longitudes,letras,P,A,B,X,ref = variables

    os.system('clear')
    print("¡Es tu turno de disparar al enemigo! Este es tu mapa:")
    print_tablero(mapas[turno])
    # Se efectua el disparo
    disparo  = input("Apunta a una coordenada: ")

    incorrecto = True
    while incorrecto: 
        if len(disparo) != 2 or disparo[0].isalpha() == False or disparo[1].isdigit() == False:
            disparo  = input("¡Ups! Prueba de nuevo: ")
        else:
            incorrecto = False
    adivina_fila = letras.index(disparo[0].upper()) + 1
    adivina_columna = int(disparo[1])
    disparo = [adivina_fila - 1, adivina_columna - 1]

    os.system('clear')


    # Veo que sucedio con el disparo
    barcos = ['poortaviones','acorazado','bote']
    ref = [P,A,B]
    longitudes = [5,3,1]
    # Veo que haya caido adentro y que no haya disparado ahi antes
    if (disparo[0] < 0 or disparo[0] > L-1) or (disparo[1] < 0 or disparo[1] > L-1):
        print("¡Uy!, eso ni siquiera esta en el océano.")
        
    elif tablero[disparo[0]][disparo[1]] == X:
        print("Ya apuntaste a esa coordenada.")
    elif tablero[disparo[0]][disparo[1]] != "O": # Tampoco X, pero se cumple
        print("Ya tocaste un barco allí.")
    elif te[disparo[0]][disparo[1]] != "O":
        for barco in range(len(barcos)):
            if te[disparo[0]][disparo[1]] == ref[barco]:
                contador[turno][barco] += 1
                tablero[disparo[0]][disparo[1]] = ref[barco]
                if contador[turno][barco] < longitudes[barco]:
                    print("Tocaste su " + barcos[barco] + ".")
                    pygame.mixer.music.play()##
                else:
                    print("¡Hundiste su " + barcos[barco] + "!")
                    pygame.mixer.music.play()##
    else:
        print("No tocaste sus barcos, %s." %(players[turno]))
        tablero[disparo[0]][disparo[1]] = X

    print_tablero(tablero)
    if sum(contador[turno]) == sum(longitudes):
        print("¡Ganaste %s!" %(players[turno]))
        continua = False
    return continua

########################################################################
def colocobarcos(variables):
    ## Función que arma el tablero y coloca los barcos
    L,barcos,longitudes,letras,P,A,B,X,ref = variables

    # Armo el tablero
    tablero = []
    for x in range(L):
      tablero.append(['O'] * L)

    # Pongo los barcos!
    for barco in range(len(barcos)):
        LB = longitudes[barco]
        posible = False
        while not posible:
            ver_hor = [range(LB),[0]*LB] # Contador auxiliar
            opcion = randint(0,1)
            ver = True
            if opcion == 1:
                ver = False    
            if ver:
                origen = [randint(0,L-LB), randint(0,L-1)]
            else:
                origen = [randint(0,L-1), randint(0,L-LB)]
            
            for sitio in range(LB):
                if tablero[origen[0] + ver_hor[opcion][sitio]][origen[1] + ver_hor[1-opcion][sitio]] != 'O':
                    break
            else:
                for sitio in range(LB):
                    tablero[origen[0] + ver_hor[opcion][sitio]][origen[1] + ver_hor[1-opcion][sitio]] = ref[barco]
                posible = True          
    return tablero

########################################################################
def colocobarcosmp(p,variables):
    # Colocar los barcos en modo multijugador

    L,barcos,longitudes,letras,P,A,B,X,ref = variables

    # Tablero
    tablero = []
    for x in range(L):
      tablero.append(["O"] * L)    
    
    print("Hola %s, debes elegir la ubicación de tus barcos. Este es el mapa táctico:" % (p))
    print_tablero(tablero)
    
    for k in range(len(barcos)):
        os.system('clear')
        print ("Capitán %s, es hora de ubicar el %s. Ocupa %s casilleros." %(p,barcos[k], longitudes[k]))

        print_tablero(tablero)
        if longitudes[k] != 1:
            vh = input("Primero debes elegir si es vertical (v) u horizontal (h): ")
            while vh != 'v' and vh != 'h':
                vh = input("¡Ups! Prueba de nuevo. Elige vertical (v) u horizontal (h): ")    
        else:
            vh = 'v'
        origen = input("Elige la coordenada de origen (ej.: a2). ¡Ten en cuenta que debe entrar en el mapa!: ")
        incorrecto = True
        while incorrecto: 
            if len(origen) != 2 or origen[0].isalpha() == False or origen[1].isdigit() == False:
                origen = input("¡Ups! Prueba de nuevo: ")
            else:
                origen = [letras.index(origen[0].upper()), int(origen[1]) - 1]
                if (vh == 'v' and (origen[0] > L-longitudes[k] or origen[1] > L-1)) \
                or (vh == 'h' and (origen[0] > L-1 or origen[1] > L-longitudes[k])):
                    origen = input("¡Ups! Prueba de nuevo: ")
                else:
                    incorrecto = False

        for place in range(longitudes[k]):
            if vh == 'v':
                tablero[origen[0]+place][origen[1]] = ref[k]
            else:
                tablero[origen[0]][origen[1]+place] = ref[k]
    return tablero
