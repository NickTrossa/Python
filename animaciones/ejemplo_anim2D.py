#!/usr/local/bin/conda3
# -*- coding: utf-8 -*-
from animacion2D import animacion2D
import numpy as np

def oscilador_am(t):
	return np.sin(2*np.pi*t) * np.exp(-t/10.)

animacion2D(oscilador_am,0,50,0.05,x='Tiempo',y='Amplitud',title='Oscilador amortiguado')
