# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 23:51:27 2014

@author: alumno
"""
'''
El formato de los códigos es, como habréis podido observar:
[A;Bm

A es un dígito que indica formato:
0 - normal
1 - negrita
2 - diluir
3 - cursiva
4 - subrayado
5 - parpadeo lento
6 - parpadeo rápido
7 - negativo (invertir)

B es un número que indica el color:
30-39 - color de texto, intensidad normal
40-49 - color de fondo, intensidad normal
90-99 - color de texto, intensidad fuerte
100-109 - color de fondo, intensidad fuerte
'''
#from termcolor import colored
#print chr(27)+"[1;36m"+"este texto sale azul"
#print chr(27)+"[0;46m"+"este texto sale con fondo azul"+chr(27)+"[0m"
#print colored('Hola mundo','red')
for col in range(10):
    print "\033[0;" + str(30+col) + "m Hola mundo"
    '''
    gris oscuro    30
    rojo            31
    verde
    amarillo
    azul
    violeta
    turquesa
    blanco
    gris claro
    '''
raw_input(" ")

startrojo = "\033[0;31m"
print startrojo + 'Soy rojo' + "\033[0;0m" + 'o no lo soy'
print "\033[0;0m" + 'Soy rojo?'