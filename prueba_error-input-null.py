#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-
"""
Distingue floats, enteros, fracciones
"""
def que_es(entrada):
	# Veo que no esté vacío
	if entrada == '':
		return 'error'
	if entrada[0] == '-':
		entrada = entrada[1:]
	# Veo si es un entero
	try:
		int(entrada)
		return 'int'
	except ValueError:
		pass
	# Veo si es un cociente de enteros
	k = []
	for i in range(len(entrada)):
		if not entrada[i].isdigit():
			if entrada[i] != '/':
				break
			else:
				k.append(i)
				if len(k) != 1 or i == len(entrada)-1:
					break
	else:
		return 'frac'
	# Veo si es un float
	try:
		float(entrada)
		return 'float'
	except ValueError:
		pass
	# Veo si es una expresión que puedo evaluar
	try:
		eval(entrada)
		return 'expr'
	except:
		return 'error'

a = input('Ponga el valor: ')
st = que_es(a)
print(st)
