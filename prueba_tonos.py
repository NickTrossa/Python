#!/opt/anaconda3/bin/python

import os

"""
Ojo! Para que funcione debe estar instalado el paquete 'sox' de linux
"""


tiempo_tot = float(input("Segundos? _> "))
frec = float(input("Frecuencia? _> "))
print("Sonando durante %.2f segundos a %.2f Hz"%(tiempo_tot,frec))
print("Para detener presione Ctr+C")
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (tiempo_tot, frec))
