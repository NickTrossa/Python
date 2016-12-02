# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 23:29:13 2014

@author: alumno
"""
# Dibuja el tablero agregando el número de fila y columna a los costados
def print_tablero(tablero):
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
