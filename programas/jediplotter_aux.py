# -*- coding: utf-8 -*-

### Graficador ###
import matplotlib.pyplot as plt
# Función que abre ventana de gráfico y ajusta sus propiedades

def ventana():
	plt.clf()
	fig = plt.figure(1)
	fig.canvas.set_window_title('Jedi Plotter 2.0')	
	plt.grid(True)
	plt.xlabel('x')
	plt.ylabel('y(x)')
	plt.title('Gráfico')
	plt.draw()
	# plt.show(block=False)
	return fig

# Función auxiliar para ver opciones
def opciones(variables, def_var, ydata):
	# entrada = input("Escribe 'config' para editar la ventana de gráfico.\nEscribe 'funciones' para ver algunos ejemplos.\n>> ")
	entrada = input("\nConfigurar ejes?\t\t[c]\nLimpiar figura?\t\t\t[l]\nVer ejemplos de funciones?\t[f]\n\
Ir a configuración avanzada\t[a]\nVolver al menú principal...\t[v]\n>> ")
	if entrada == 'c':
		print("Límites del gráfico...")
		autoconfigurar = input('Autoconfigurar? [y]/n ')

		if autoconfigurar == 'n':
			def asigno_var(va, clave, texto):
				entrada = input(texto)
				if entrada != '':
					return float(entrada)
				else:
					return va[clave]				
			variables['xinf'] = asigno_var(variables, 'xinf', 'Abscisa inferior: ')
			variables['xsup'] = asigno_var(variables, 'xsup', 'Abscisa superior: ')
			variables['yinf'] = asigno_var(variables, 'yinf', 'Ordenada inferior: ')
			variables['ysup'] = asigno_var(variables, 'ysup', 'Ordenada superior: ')

		else:
			if not(ydata is None):
				if input("Ejes por defecto?\t [d]\nModo inteligente?\t [i]\n>> ") == 'i':
					# Autoconfigurar el límite de los ejes: elije el intervalo mínimo para y entre el default y los datos
					#Indices auxiliares que voy a necesitar
					puntos_totales = (def_var['xf']-def_var['x0'])*def_var['densidad']
					n_xinf = int((def_var['xinf']-def_var['x0'])*puntos_totales/(def_var['xf']-def_var['x0']))
					n_xsup = int((def_var['xsup']-def_var['x0'])*puntos_totales/(def_var['xf']-def_var['x0']))

					yinf = min(ydata[n_xinf:n_xsup])
					ysup = max(ydata[n_xinf:n_xsup])

					dy = (ysup-yinf)*0.01
					yinf -= dy
					ysup += dy

					variables['yinf'] = max(yinf,def_var['yinf'])
					variables['ysup'] = min(ysup,def_var['ysup'])
				else:
					variables = def_var
					print(def_var)
			
	elif entrada == 'l':
		fig = ventana()
	elif entrada == 'v':
		print("\nMenú principal...")
	elif entrada == 'a':
		if input("¿Modificar límtes a computar? [n]/y: ") == 'y':
			variables['x0'] = float(input('x0 (mínimo valor a evaluar): '))
			variables['xf'] = float(input('xf (máximo valor a evaluar): '))
			variables['densidad'] = float(input('Densidad: '))

	elif entrada == 'f':
		print('y1(x) = sin(2*pi*x) \ny2(x) = x**2 - 1 \ny3(x) = log10(x) \ny4(x) = log(x)')

	else:
		print("No has elegido ninguna opción.")

	return variables





