#!/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

### Graficador ###
'''
COSAS QUE FALTAN:

Agregar opción para graficar algo que tenga un parámetro libre.

Buscar funciones para agregar en la ayuda
Agregar autoconfigurar ejes

Agregar criterio de las intersecciones.
'''
from matplotlib.pylab import *
#import numpy as np
#import matplotlib.pyplot as plt

# clf, figure, grid, xlabel, ylabel, title, plot, legend, draw, show, axis, savefig
# linspace
from datetime import datetime
from jediplotter_aux import opciones, ventana

print("## ---> Jedi Plotter 2.0 <--- ##")

# Configuraciones de gráfico iniciales
fig = ventana()

# Variables por defecto
def_var = {
	'xinf': -10.0,
	'xsup': 10.0,
	'yinf': -10.0,
	'ysup': 10.0,
	'x0': -100.0,
	'xf': 100.0,
	'densidad': 1000,
	}

default_var = True
var = def_var
ydata = None
count = 0
funciones = []
while True:
	count += 1
	if count>1:
		deseo = input("\nSeguir graficando?\t [g]\nOpciones?\t\t [op]\nSalir?\t\t\t [q]\nGuardar y salir?\t [qs]\n>> ")
	else:
		deseo = input("\nGraficar?\t [g]\nOpciones?\t [op]\nSalir?\t\t [q]\nGuardar y salir? [qs]\n>> ")
	if deseo == 'g':
		expr = input("y(x) = ")

		# Armado de la dispersión de puntos
		puntos_totales = (var['xf']-var['x0'])*var['densidad']
		x = linspace(var['x0'],var['xf'],puntos_totales+1)
		#x = x.astype('complex')
		y = eval(expr)
		#xdata = x.real
		#ydata = y.real

		# Defino valores de los ejes
		if default_var:
			#var = autoconfig(var, y)
			axis((def_var['xinf'],def_var['xsup'],def_var['yinf'],def_var['ysup']))

		# Grafico
		plot(x, y, lw=2, label=expr)
		legend()
		draw()
		show(block=False)
	elif deseo == 'op':
		default_var = False

		var = opciones(var, def_var, ydata)

		axis((var['xinf'],var['xsup'],var['yinf'],var['ysup']))
		draw()
	elif deseo == 'qs':
		nombre = 'figura_'+str(datetime.now())+'.png'
		savefig('/home/nicolas/Desktop/%s'%(nombre))
		print('Figura guardada en el escritorio como "%s". \n### Fin del programa. ###'%(nombre))
		break
	elif deseo == 'q':
		print("### Fin del programa. ###")
		break
	else:
		print("Ups! Prueba de nuevo\n")
