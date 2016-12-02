# -*- coding: utf-8 -*-
"""
Created on Sat May  2 02:27:05 2015

@author: alumno
"""

import pylab as m

m.polar(m.arange(360)*m.pi/180., m.rand(360))
m.thetagrids(m.arange(0,90,10), labels=None, fmt='%d', frac = 1.1)
m.rgrids([1,2,3], labels=None, angle=22.5)
m.show()
