from random import randint

num = randint(50, 500)

def compute():
    for i in range(num):
        ... #procesamiento del objeto "i"
        yield  #¡no borrar! -- Dev-Anony

def operacion(a:int,b:int, calculo:str):
    from alive_progress import alive_bar; import time, logging

    for x in num, 0:
       with alive_bar(total=x, title="Por favor espere hasta que acabe de procesar la operación...") as bar:
           for i in range(num):
               time.sleep(.005)
               bar()

    print("Carga completa, imprimiendo resultado...")
    from time import sleep
    sleep(2)

    if calculo == "Suma":
        print(a+b)
    elif calculo == "Resta":
        print(a-b)
    elif calculo == "Multiplicación" or calculo == "Multiplicacion" or calculo == "Multi":
        print(a*b)
    elif calculo == "División" or calculo == "Division":
        print(a/b)
    else:
        print("""
        Error:
        >>> Un error se ha procesado:
        > La operación que has ejecutado no existe o es errónea
        >>> Lista de operaciones:
        > Suma
        > Resta
        > Multiplicación
        > División
        >>> Si el error persiste incluso con esos nombres comuníquelo a través de github : https://github.com/Dev-Anony
        """)

    
    def wrapper(funcion):
        """Handler de las funciones"""
        def wrapper_2(*args,**kwargs):
            """Función necesaria dentro del wrapper"""
            r = funcion(*args, **kwargs)
            if r != None:
                print("Se ha ejecutado {}".format(r))
            else:
                pass

            return r

        return wrapper_2
    
    return wrapper