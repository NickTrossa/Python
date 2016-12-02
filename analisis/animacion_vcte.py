# -*- coding: utf-8 -*-

# Programa para alinear el instrumental en la práctica del efecto fotoeléctrico usando un LockIn 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from math import *
import visa


def Vcte(V,inttime,Tiempo):
    '''
    Grafica el voltaje tomado del LockIn usando un tiempo de integración 'inttime' (en segundos- ver time_cnt)
    durante 'Tiempo' segundos con un voltaje del generador interno seteado en 'V' volts.
    '''
    # Diccionario auxiliar para convertir tiempo al código que reconoce el Lockin
    time_cnt = [1e-3,2e-3,3e-3,10e-3,30e-3,100e-3,300e-3,1,2,3,10,30,100]
    numeros = range(1,12)
    tc_dict = dict(zip(time_cnt,numeros))
    #---------------------------------------------------------------
    # Abro la sesión con el LockIn y seteo V y inttime
    rm = visa.ResourceManager()
    print(rm.list_resources())
    
    lockin = rm.open_resource('GPIB0::22::INSTR')
	
    lockin.write('T1 ,',str(tc_dict[inttime]))
    lockin.write('X5 ,',str(V))
    
    #---------------------------------------------------------------
    ## Armo los puntos a plotear: voltaje vs. tiempo
    t0 = time.time()
    def generopuntos():
        t = 0
        while t < Tiempo:
            t = time.time()-t0
            yield t, t#float(lockin.query('Q'))   
    generador = generopuntos()
    #---------------------------------------------------------------
    ## Creo la figura con sus propiedades
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    plt.axis((0,30,-1,2))
    plt.grid()
    plt.xlabel('Tiempo')
    plt.ylabel('Voltaje')
    plt.title('Prueba de alineación')
    #---------------------------------------------------------------
    ## Defino la función que va a crear los cuadros de la animación
    xdata, ydata = [], []
    def run(data):
        # update the data
        t,y = data
        xdata.append(t)
        ydata.append(y)
        # Ejes movibles
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        if y >= ymax or y <= ymin:
            ax.set_ylim(ymin, 2*ymax)
            ax.figure.canvas.draw()
        line.set_data(xdata, ydata)
        return line,
	#---------------------------------------------------------------
	## LLamo a la función mágica que hace el trabajo
    ani = animation.FuncAnimation(fig, run, generador, blit=True, interval=4*inttime)
    #repeat=False
    plt.show()

    lockin.close()
