# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 21:08:49 2015

@author: alumno
"""
from math import pi
#pi = 3.14159265358979323846
class Constante(object):
    def __init__(self,nombre,valor,unidades, sist_unidades):
        self.nom = nombre
        self.val = valor
        self.un = unidades
        self.sist_unidades = sist_unidades
    
    def convertto(self, sistema):
        if self.sist_unidades == sistema:
            print("Ya está en ese sistema de unidades.")
        else:
            if sistema == 'cgs':
                aux = -1
                self.sist_unidades = 'cgs'
            elif sistema == 'mks':
                aux = 1
                self.sist_unidades = 'mks'
            for k in range(2):
                for magnitud in self.un[k]:
                    if magnitud == 'M':
                        self.val *= 1e3**(aux*((-1)**k))
                    elif magnitud == 'L':
                        self.val *= 1e2**(aux*((-1)**k))
                    elif magnitud == 'C':
                        self.val /= (1/3.335641e-10)**(aux*((-1)**k))
    def propiedades(self):
        print("Nombre:", self.nom)
        print("Valor:", str(self.val))
        print("Sistema de unidades:", self.sist_unidades)
        print("Unidades involucradas:", str(self.un))
            
            
hbar = Constante("cte de planck normalizada", 1.054571628e-34, ('MLL','T'), 'mks')
h = Constante("cte de planck", 6.62606896e-34, ('MLL','T'), 'mks')
c = Constante("velocidad de la luz en el vacío", 299792458.0, ('L','T'), 'mks')
e = Constante("carga del electrón", 1.602176565e-19, ('C',''), 'mks')
me = Constante("masa del electrón", 9.10938291e-31, ('M',''), 'mks')
mp = Constante("masa del protón", 1.672621777e-27, ('M',''), 'mks')
eps0 = Constante("Constante dieléctrica del vacío", 8.8541878176e-12, ('C C T T','D D D M'), 'mks')

print("Bienvenido a la calculadora de constantes en sistema mks. Has cargado las siguientes constantes:")

print("""
hbar = 1.054571628e-34  # cte de planck normalizada
h = 6.62606896e-34      # cte de planck
c = 299792458           # velocidad de la luz en el vacío
e = 1.602176565e-19     # carga del electrón
me = 9.10938291e-31     # masa del electrón
mp = 1.672621777e-27    # Masa del protón
eps0 = 8.8541878176e-12 # Constante dieléctrica del vacío
pi = 3.14159265358979323846
""")

print("Ahora puedes operar en la consola...")
