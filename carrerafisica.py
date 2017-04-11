#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:44:54 2015

@author: alumno
"""

notascbc = {
"ICSE": 10,
"IPC": 9,
"Análisis Matemático": 8,
"Álgebra": 8,
"Química": 7,
"Física": 9
}

notas = {
"Matemática 1" : 9,
"Matemática 2": 10,
"Matemática 3": 4,
"Matemática 4": 9,
"Física 1": 7,
"Física 2": 10,
"Física 3": 9,
"Física 4": 10,
"Mecánica Clásica": 9,
"Laboratorio 1": 8,
"Laboratorio 2": 8,
"Laboratorio 3": 9,
"Laboratorio 4": 9,
"Laboratorio 5": 9,
"Laboratorio 6": 9,
"Laboratorio 7": 9,
"Estrucura 1": 10,
"Estrucura 2": False,
"Estrucura 3": False,
"Estrucura 4": False,
"Física Teórica I": 10,
"Física Teórica II": 9,
"Física Teórica III": False,
"Cálculo Numérico": 10,
"Labo de Electrónica": 10,
"Incertezas experimentales": 10,
"Optativa 3": False
}

#concbc = 0
#while not isinstance(concbc,bool):
concbcstring = input("¿Contamos el CBC? [s/N]: ")
concbc = (concbcstring.lower() == 's')

if concbc: notas.update(notascbc)

suma = 0.0
materiasrendidas = 0
for materia in notas:
    if not isinstance(notas[materia],bool):
        suma += notas[materia]
        materiasrendidas += 1

promedio = suma/materiasrendidas

total_materias = len(notas)
porcentaje = 100.0*materiasrendidas/total_materias

print("Has finalizado %s materias con un promedio de %s." %(materiasrendidas, '%.2f' % promedio))
print("Eso es un %%%s de la carrera." %( '%.0f' % porcentaje))
