# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:02:00 2015

@author: alumno
"""

# Modificar .txt

f = open("modificar.txt", 'w')

f.write('pppp')

f.close()


f = open("modificar.txt", 'r')

print f.read()

f.close()