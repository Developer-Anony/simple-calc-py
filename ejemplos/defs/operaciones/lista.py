def _a(a:int):
    try:
        int(a)
    except:
        print("Error")

def _b(b:int):
    try:
        int(b)
    except:
        print("Error")

def Suma(a:_a,b:_b):
    return a+b

def Restar(a:_a,b:_b):
    return a-b

def Multiplicar(a:_a,b:_b):
    return a*b

def Dividir(a:_a,b:_b):
    return a/b