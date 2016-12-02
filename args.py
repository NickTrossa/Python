"""
Un argumento puede entrar como None, pero no puede estar ausente
"""
def args(a,b):
	if not(b is None):
		return a,b		
	else:
		print("b not defined")
		return a,
b = None
res = args(3,b)
print(res)
print(type(args))
