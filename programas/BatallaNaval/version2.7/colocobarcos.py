# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 22:55:31 2014

@author: alumno
"""

def colocobarcos(variables):
    ## Función que arma el tablero y coloca los barcos
    from random import randint
    L = variables[0]
    barcos = variables[6]
    ref = variables[7]
    longitudes = variables[8]
    CB = len(barcos) # Cantidad de Barcos 
    # Armo el tablero
    tablero = []
    for x in range(L):
      tablero.append(['O'] * L)

    # Pongo los barcos!
    for barco in range(CB):
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