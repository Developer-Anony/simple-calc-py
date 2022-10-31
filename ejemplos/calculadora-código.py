import defs
from defs import calculadora

@calculadora.operacion(2,1,"Suma")
def hola():
    print("Hola mundo")

hola()