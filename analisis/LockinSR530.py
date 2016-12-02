import visa
import numpy as np

class Lockin(object):
    '''Clase para el manejo amplificador Lockin SR530 usando PyVISA de interfaz'''
    
    def __init__(self,resource):
        self._lockin = visa.ResourceManager().open_resource(resource)
        #self._lockin.query('*IDN?')
        self._lockin("I 2") #Bloquea el uso de teclas del Lockin
        
    def __del__(self):
        self._lockin("I 0") #Desbloquea el Lockin
        self._lockin.close()

        '''
    def setModo(self, modo):
        '''Selecciona el modo de medición, A [modo = 0], A-B [1], I [2], I(10M) [3]'''
        self._lockin.write("ISRC {0}".format(modo))
        
    def setFiltro(self, sen, tbase, slope):
        '''Setea el filtro de la instancia'''
        #Página 23 del manual
#        self._lockin.write("OFLS {0}".format(slope))
        self._lockin.write("T1 {0}".format(tbase)) 
        self._lockin.write("SENS {0}".format(sen)) 
        
    def setAuxOut(self, auxOut = 1, auxV = 0):
        '''Setea la tensión de salida de al Aux Output indicado.
        Las tensiones posibles son entre -10.5 a 10.5'''
        self._lockin.write('AUXV {0}, {1}'.format(auxOut, auxV))
            '''
    def setReferencia(self,isIntern, freq, vRef = 1):
        if isIntern:
            #Referencia interna
            #Configura la referencia si es así
            self._lockin.write("FMOD 1")
            self._lockin.write("SLVL {0:f}".format(voltaje))
            self._lockin.write("FREQ {0:f}".format(freq))
        else:
            #Referencia externa
            self._lockin.write("FMOD 0")
        '''    
    def setDisplay(self, isXY):
        if isXY:
            self._lockin.write("DDEF 1, 0") #Canal 1, x
            self._lockin.write('DDEF 2, 0') #Canal 2, y
        else:
            self._lockin.write("DDEF 1,1") #Canal 1, R
            self._lockin.write('DDEF 2,1') #Canal 2, T
    
    def getDisplay(self):
        '''Obtiene la medición que acusa el display. 
        Es equivalente en resolución a la medición de los parámetros con SNAP?'''
        orden = "SNAP? 10, 11"
        return self._lockin.query_ascii_values(orden, separator=",")
        
    def getMedicion(self,isXY = True):
        '''Obtiene X,Y o R,Ang, dependiendo de isXY'''
        orden = "SNAP? "
        if isXY:
            self._lockin.write("DDEF 1,0") #Canal 1, XY
            orden += "1, 2" #SNAP? 1,2
        else:
            self._lockin.write("DDEF 1,1") #Canal 1, RTheta
            orden += "3, 4" #SNAP? 3, 4
        return self._lockin.query_ascii_values(orden, separator=",")
'''
