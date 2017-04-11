Las clases tienen atributos (funciones-"métodos"- o variables) definidas en ellas:

class MiClase:
    atributo1 = 3.1415
    def atributo2(self):
        return "hola"

"Instantation" es la accion de crear un objeto(instancia) de esa clase:
objeto = MiClase(args)

que, naturalmente, tendrá los atributos de ella.
Cuando se crea, automaticamente se invoca el método __init__(self,args)

