# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:00:55 2015

@author: alumno

Preliminares
"""

### Recorto el comienzo ###

# Filtro altas frecuencias para suavizarla y contar mejor los picos
def filtro(data,fc,fs=1):
    import numpy as np
    N = len(data)
    tf = np.fft.fft(data)
    fcc = fc/fs
    for i in range(round(fcc*N),int(N/2)):
        tf[i] = 0
        tf[N-i] = 0    
    return np.real(np.fft.ifft(tf))

### Defino el umbral ###
def calc_umbral_2(amplitud,bajada=0.2):
    import numpy as np
    def umbral_sec(ampli):
        """
        Calculo el umbral con la media de los valores que toma la amplitud, menos un poquito
        """
        ma = max(ampli)
        mi = min(ampli)
        M = (ma+mi)/2        
        return M - bajada * (M-mi)
    ya = umbral_sec(amplitud[:1000])
    yb = umbral_sec(amplitud[-1000:])
    return np.arange(len(amplitud))*(yb-ya)/len(amplitud)+ya

## Busco minimos
def busco_minimos(vec,umbral,cp=0):
    import numpy as np
    mins = []
    for i in range(2,len(vec)-2):
        if vec[i] < umbral[i] and\
        vec[i] < vec[i-1] and vec[i] <= vec[i+1]:
            mins.append(i)
    return np.array(mins)

## Saco los minimos que estan fuera de lugar con el criterio del cociente
def saco_minimos(mins):
    from scipy.stats import mode
    import numpy as np
    aux = mins[1:]-mins[:-1]
    delta = mode(aux)[0][0]
    newmins = []
    for i in range(1,len(mins)-1):
        if round(aux[i-1]/delta)==1 or round(aux[i]/delta)==1:
            newmins.append(mins[i])
    ## Segundo filtro: de los pegados me quedo con uno
    newmins2 = []
    aux2 = np.array(newmins[1:])-np.array(newmins[:-1])
    for i in range(len(aux2)-1):
        if aux2[i] > 0.5*np.std(aux2):
            newmins2.append(newmins[i])
    return np.array(newmins2)

### Cuerpo del programa ###
def armo_secuencia(vec,mins,prop=0.03):
    from scipy.stats import mode
    """
    prop es la proporcion de la fibrilacion en relacion al alto de la señal (3% por defecto)
    """
    ## Distancia típica entre minimos
    dt = mode(mins[1:]-mins[:-1])[0][0]
    
    fibrilaciones = []
    dudosos = []
    ## Auxiliar para contar distancia entre valles
    analizados = []
    ## Listas auxiliares para graficar
    minglob = []
    maxglob = []
    for i in range(len(mins)-1):
        minloc = []
        maxloc = []    
        ## VERIFICO QUE LA DISTANCIA ENTRE MINIMOS SEA CORRECTA
        anchorelativo = (mins[i+1]-mins[i])/dt
        analizados.append(anchorelativo)
        if round(anchorelativo) == 1:
            ## Busco los minimos y maximos locales en el periodo
            for j in range(mins[i]+1,mins[i+1]-1):
                if vec[j] < vec[j-1] and vec[j] <= vec[j+1]:
                    minloc.append(j)
                    minglob.append(j)
                if vec[j] > vec[j-1] and vec[j] >= vec[j+1]:
                    maxloc.append(j)
                    maxglob.append(j)
            ## Busco los picos de extrasistoles definiendo una distancia h minima entre eventos
            h = prop * abs( max(vec[mins[i]:mins[i+1]]) - min(vec[mins[i]:mins[i+1]]) )
            for k in range(len(minloc)):
                if abs(vec[minloc[k]]-vec[maxloc[k]]) > h and\
                abs(vec[minloc[k]]-vec[maxloc[k+1]]) > h:
                    fibrilaciones.append(mins[i])
                    break # No puede haber más de 1 fibrilacion por ciclo
        else:
            # Asumo que todas son fibrilaciones
            for n in range(int(round(anchorelativo))):
                dudosos.append(mins[i] + 4*n)
    return fibrilaciones,dudosos,minglob,maxglob,analizados


"""
extras = 0
if input('Verificar dudosos? S/n') != 'n':
    fig, sub = subplots(1)
    line, = sub.plot([],[])
    sub.axis((0,201,min(amp),max(amp)))
    for i in range(len(duds)):
        line.set_data(arange(200),amp[(duds[i]-200):duds[i]])
        sub.relim()
        sub.autoscale_view()
        fig.canvas.draw()
        if waitforbuttonpress(10):
            extras += 1
print(extras)

figure(4),clf()
bines = arange(1,100)+.5
hist(array(mins[1:])-array(mins[:-1]),bins=bines)

#def saco_minimos(mins):
#    from scipy.stats import mode
#    import numpy as np
#    aux = mins[1:]-mins[:-1]
#    inta = mode(aux)[0][0] - 1*np.std(aux)
#    intb = mode(aux)[0][0] + 1*np.std(aux)
#    newmins = []
#    ## Primer filtro: grandes gaps
#    for i in range(1,len(mins)-1):
#        if (aux[i-1] < intb and aux[i-1] > inta) or\
#        (aux[i] < intb and aux[i] > inta):
#            newmins.append(mins[i])
#    newmins = np.array(newmins)
#    ## Segundo filtro: de los pegados me quedo con uno
#    aux2 = newmins[1:]-newmins[:-1]
#    newmins2 = newmins
#    for i in range(len(aux2)):
#        if aux2[i] < 0.5*np.std(aux2):
#            del newmins2[i]
#    
#    return newmins,np.array(newmins2)


def calc_umbral(amplitud):
    import matplotlib.pyplot as plt
    import numpy as np
    '''
    Calculo el umbral con el promedio de la altura de los mins más un std
    '''
    def umbral_sec(ampli):
        mins = minimos(ampli)
        amps = ampli[mins]
        
        plt.figure()
        h0 = plt.hist(amps,normed=True,bins=np.sqrt(len(amps)))
        media = np.mean(amps)
        stdev = np.std(amps)
        plt.vlines(media,0,max(h0[0]),colors='r')
        plt.vlines(media-stdev,0,max(h0[0]),colors='k')
        plt.vlines(media+stdev,0,max(h0[0]),colors='k')
        
        return media + 3*stdev/2
    ya = umbral_sec(amplitud[:1000])
    yb = umbral_sec(amplitud[-1000:])
    
    return np.arange(len(amplitud))*(yb-ya)/len(amplitud)+ya
"""