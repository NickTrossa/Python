# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:56:20 2015

@author: alumno
"""
import time
while True:
    print('sigue...')
    time.sleep(0.5)
    i = input("Enter text (or Enter to quit): ")
    if not i:
        break
    print("Your input:", i)
print("While loop has exited")