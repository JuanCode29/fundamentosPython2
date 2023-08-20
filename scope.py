var = 100 # scope global
def doble():
    global resultado;
    global var;
    var = var + 100
    resultado = var * 2
    return resultado
print(doble())
print(var)
print(resultado)