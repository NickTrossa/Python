# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:34:00 2016

@author: nicolas
"""

"""
Programa que lista todos los .DAT en el directorio y los subdirectorios
"""

from os import walk

mypath = '/home/nicolas/Dropbox/Labo6&7 Juanma-Nico/Mediciones KP/Orito1/Au'

def get_paths(directorio):
    n= len(directorio)
    paths = []
    for (dirpath, dirnames, filenames) in walk(directorio):
        for i in filenames:
            if i[-4:] == '.DAT':
                paths.append(dirpath[n:] + '/' + i)
    return paths
mostrame(get_paths(mypath))