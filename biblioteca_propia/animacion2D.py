#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-
def animacion2D(funcion,t0,tf,dt,x='x',y='y',title='Título', auto=False):
	"""
	funcion es la funcion que se va a graficar
	x0,xf - intervalo
	auto - True si quiero seguir la curva de cerca
	OJO: auto=True NO FUNCIONA
	"""
	import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.animation as animation

	###############################
	# Iterador que genera los puntos evaluando la funcion
	def data_gen(t0,tf,dt):
		t = t0
		while t <= tf:
			t += dt
			yield t, funcion(t)
	

	###############################
	# Creo la figura con los ejes y las etiquetas
	fig, ax = plt.subplots()
	line, = ax.plot([], [], lw=2)
	ax.set_xlabel(x)
	ax.set_ylabel(y)
	ax.set_title(title)
	ax.grid()	
	###############################
	# Defino límites de los ejes	
	values = funcion(np.linspace(t0,tf,int((tf-t0)/dt+1)))
	ax.set_ylim(min(values),max(values))
	if not auto:
		ax.set_xlim(t0, tf)

	# Iterable que actualiza los frames
	xdata, ydata = [], []
	def run(data):
		t,y = data
		xdata.append(t)
		ydata.append(y)
		if auto:
			xmin, xmax = ax.get_xlim()
			if t >= xmax:
				ax.set_xlim(xmin, 2*xmax)
				#ax.figure.canvas.draw()
			line.set_data(xdata, ydata)
			return line,
		else:
			line.set_data(xdata, ydata)
			return line,

	ani = animation.FuncAnimation(fig, run, data_gen(t0,tf,dt),\
		blit=True, interval=10, repeat=False)
	plt.show()
