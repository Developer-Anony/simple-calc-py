def nueva(nombre:str=None, descripcion:str=None):
    if nombre==None and descripcion==None:
        a = ""
    elif nombre!=None and descripcion==None:
        a = " {}".format(nombre)
    elif nombre==None and descripcion!=None:
        a = " ({})".format(descripcion)
    else:
        a = " {} ({})".format(nombre, descripcion)
    
    def wrapper(funcion):
        def wrapper_2(*args,**kwargs):
            res = funcion(*args, **kwargs)
            print("Se ha ejecutado{}".format(a))

            return res

        return wrapper_2
    
    return wrapper