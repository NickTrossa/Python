# -*- coding: utf-8 -*-
def animacion3D(x,y,z,title,save=False,salteo=10,interval=1,fps=15):
	"""
	A simple example of an animated plot... In 3D!
	x,y,z 'arrays' de posición para cada tiempo
	title 'string'
	save 'bool' True si desea guardar el video
	limits 'tupple' con los límites (xmin,xmax,ymin,ymax,zmin,zmax)
	"""
	import matplotlib.pyplot as plt
	import mpl_toolkits.mplot3d.axes3d as p3
	import matplotlib.animation as animation

	frames=int(len(x)/salteo)
	def update_lines(num,x,y,z,line) :
		num *= salteo
		# NOTE: there is no .set_data() for 3 dim data...
		line.set_xdata(x[:num])
		line.set_ydata(y[:num])
		line.set_3d_properties(z[:num])
		return line

	# Attaching 3D axis to the figure
	fig = plt.figure(3)
	ax = p3.Axes3D(fig)
	ax.view_init(azim=225,elev=None)
	# Creating fifty line objects.
	# NOTE: Can't pass empty arrays into 3d version of plot()
	line = ax.plot(x[0:1], y[0:1], z[0:1])[0]

	# Setting the axes properties
	ax.set_xlim3d([min(x) , max(x)])
	ax.set_xlabel('X')

	ax.set_ylim3d([min(y) , max(y)])
	ax.set_ylabel('Y')

	ax.set_zlim3d([min(z) , max(z)])
	ax.set_zlabel('Z')

	ax.set_title(title)

	# Creating the Animation object
	anim = animation.FuncAnimation(fig, update_lines, fargs=(x,y,z, line),
		                          interval=interval, blit=False, frames=frames )
	if save==True:
		direx = input('Ingrese el directorio de guardado de la animacion: /')
		anim.save('/%s/%s.mp4'%(direx,title), fps=fps, extra_args=['-vcodec', 'libx264'])
		print('Animacion guarada en %s'%direx)
	else:
		print("Animación comenzada...")
		plt.show()
