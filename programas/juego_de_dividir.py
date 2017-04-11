#!/opt/anaconda3/bin/python
from random import random
dividendo = 1000 + int(1e5*random())
divisor = 10 + int(490*random())
print("Dividendo:",dividendo)
print("Divisor:",divisor)
input()
print(dividendo/divisor)
