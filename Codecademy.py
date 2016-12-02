# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 03:40:42 2014

@author: alumno
"""
###################################
def suma_de_digitos(n):
    ns = str(n)
    a=0
    for i in range(len(ns)):
        a += int(ns[i])
    return a

###################################
# Zip
x = range(5)
y = range(3,9)
for xd,yd in zip(x,y):
    print(xd,yd)
    
###################################
from math import log10
def suma_de_digitos2(n):
    a=0
    digits = int(log10(n)) + 1
    if log10(n) % 1 != 0:
        digits += 1
    ns=[]
    suma = 0
    for i in range(digits):
        ns.append(n % 10**(i+1) - suma)
        suma += ns[i]
        a += int(ns[i]/(10**(i)))
    return a
    
###################################
def factorial(x):
    f=1
    for i in range(x):
        f *= (i+1)
    return f

###################################    
def es_primo(x):
    if x<2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
                break
        else:
            return True

###################################
def reverse(texto):
    L=len(texto)
    rev=[]
    for i in range(L):
        rev.append(L-1-i)
    inv=""
    for i in rev:
        inv += texto[i]
    return inv
    
###################################
def anti_vocal(texto):
    cons = ""
    vocales = ['a','e','i','o','u']
    for letra in texto:
        for voc in vocales:
            if letra.lower() == voc:
                break
        else:
            cons += letra
    return cons

###################################
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 8, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 5, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 8, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
###################################
def censor(texto,palabra):
    lista = texto.split()
    for pal in lista:
        if pal == palabra:
            lista[lista.index(pal)]= "*" * len(pal)
    return " ".join(lista)
    
###################################
def contar(secuencia,item):
    contados = 0
    for elem in secuencia:
        if elem == item:
            contados += 1
    return contados
    
###################################
    def purificar(lista):
    purif = []
    for num in lista:
        if num % 2 == 0:
            purif.append(num)
            #print "    removido"
    return purif


###################################
def producto(lista):
    prod = 1
    for num in lista:
        prod *= num
    return prod
    
###################################
    def eliminar_repetidos(lista):
    rest = []
    for num in lista:
        for rnum in rest:
            if num == rnum:
                break
        else:
            rest.append(num)
    return rest

###################################
def media(lista):
    orden = sorted(lista)
    L = len(lista)
    if L % 2 == 0: # L par
        media = (orden[L/2-1] + orden[L/2])/2.0
    else:
        media = orden[(L-1)/2]
    return media

###################################
calificaciones = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50,5]

def notes_sum(calificaciones):
    suma = 0
    for cal in calificaciones:
        suma += cal
    return suma
notes_sum(calificaciones)

###################################
compras = ["banana", "naranja", "manzana"]

inventario = {
    "banana": 6,
    "manzana": 0,
    "naranja": 32,
    "pera": 15
}
    
precios = {
   'naranja': 1.5, 'pera': 3, 'banana': 4, 'manzana': 2
}

# Escribí tu código acá.
def calcular_factura(comida):
    total = 0
    for i in comida:
        if inventario[i] > 0:
            total += precios[i]
            inventario[i] = inventario[i] - 1
    return total

###################################

###################################
