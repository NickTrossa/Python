#!/usr/local/bin/python3

"""
Llamando 
python3 programa.py $variable
puedo, con sys.argv, crear una lista con las variables que vienen de afuera (bash)
"""
import sys

print(type(sys.argv))
print(sys.argv)

#output = open('muestronum.txt', 'w')
#output.write(str(numero))
#output.close()
