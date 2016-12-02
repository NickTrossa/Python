#!/usr/local/bin/conda3

from cmath import sqrt as csqrt
from math import sqrt
from fractions import Fraction
print("### Bienvenido a la calculadora de raíces de f(x) = ax^2 + bx + c")

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

def separo(frac):
	k = [i for i in range(len(frac)) if frac[i] == '/']
#	print(frac)
#	print(k)
	return Fraction(int(frac[:k[0]]), int(frac[(k[0]+1):]))
##########################################################################################
# Pido los coeficientes
while True:
	coeff = [0,0,0]
	names = ['a','b','c']
	tipos = {'int':0,'frac':1,'float':2,'expr':3,'error':4}
	tip = [0,0,0]
	for i in range(3):
		while True:
			coeff[i] = input("Ingrese el valor de '%s': "%names[i])
			tip[i] = tipos[que_es(coeff[i])]
			if tip[i] != 4:
				break
			else:
				print("Ups! Prueba de nuevo...")

	# Defino qué tipos de coeficientes voy a manejar
	vv = max(tip)

##########################################################################################	
	if vv == 0:
		a = int(coeff[0])
		b = int(coeff[1])
		c = int(coeff[2])
		det = b**2-4*a*c
		if det < 0:
			print('No tiene raíces reales')
			r1 = (-b-csqrt(complex(det)))/2/a
			r2 = (-b+csqrt(complex(det)))/2/a
			print('Las raíces son:\n--> x1 = ' + str(r1) + '\n--> x2 = ' + str(r2))
		elif det == 0:
			print("Tiene raíces dobles...")
			r = -Fraction(b,2*a)
			if r.denominator == 1:
				r = r.numerator
				print('Las raíces son:\n--> x1 = x2 = ' + str(r))
			else:	
				print('Las raíces son:\n--> x1 = x2 = ' + str(r.numerator)+ '/' + str(r.denominator))
		else:
			raiz = sqrt(det)
			print('Las raíces son:\n')
			if raiz.is_integer():
				R = [Fraction(-b-int(raiz),2*a), Fraction(-b+int(raiz),2*a)]
				for n in range(2):
					if R[n].denominator == 1:
						R[n] = R[n].numerator
						print('--> x%i = '%(n+1) + str(R[n]))
					else:
						print('--> x%i = '%(n+1) + str(r.numerator)+ '/' + str(r.denominator))
			else:
				print('--> x1 = (- %i - sqrt{%i} )/ %i'%(b,det,2*a))
				print('--> x2 = (- %i + sqrt{%i} )/ %i'%(b,det,2*a))
##########################################################################################	
	elif vv == 1:
		# Transformo a fracción
		a = separo(coeff[0]) if tip[0] == 1 else int(coeff[0])
		b = separo(coeff[1]) if tip[1] == 1 else int(coeff[1])
		c = separo(coeff[2]) if tip[2] == 1 else int(coeff[2])
		det = b**2-4*a*c
		if det < 0:
			print('No tiene raíces reales')
			r1 = (-b-csqrt(complex(det)))/2/a
			r2 = (-b+csqrt(complex(det)))/2/a
			print('Las raíces son:\n--> x1 = ' + str(r1) + '\n--> x2 = ' + str(r2))
		elif det == 0:
			print("Tiene raíces dobles...")
			r = -Fraction(b,2*a)
			if r.denominator == 1:
				r = r.numerator
				print('Las raíces son:\n--> x1 = x2 = ' + str(r))
			else:	
				print('Las raíces son:\n--> x1 = x2 = ' + str(r.numerator)+ '/' + str(r.denominator))
		else:
			raiz_num = sqrt(det.numerator)
			raiz_den = sqrt(det.denominator)
			print('Las raíces son:\n')
			if raiz_num.is_integer() and raiz_den.is_integer():
				raiz = Fraction(raiz_num,raiz_den)
				R = [Fraction(-b-raiz,2*a), Fraction(-b+raiz,2*a)]
				for n in range(2):
					if R[n].denominator == 1:
						R[n] = R[n].numerator
						print('--> x%i = '%(n+1) + str(R[n]))
					else:
						print('--> x%i = '%(n+1) + str(r.numerator)+ '/' + str(r.denominator))
			else:
				a1 = a.numerator
				a2 = a.denominator
				b1 = b.numerator
				b2 = b.denominator
				print('--> x1 = (- %i - %i*sqrt{%i/%i} )/ %i'%(b1*a2,a2,det.numerator,det.denominator,2*a1*b2))
				print('--> x1 = (- %i + %i*sqrt{%i/%i} )/ %i'%(b1*a2,a2,det.numerator,det.denominator,2*a1*b2))
##########################################################################################	
	else:
		print('A desrrollar...(no uses números con coma ni irracionales)')

	if input("\n¿Calcular más raíces? [s]/n \n>> ") == 'n':
		print("Fin del programa")
		break

