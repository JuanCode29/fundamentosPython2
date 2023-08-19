var = 100 # scope global
def doble():
    global resultado;
    resultado = var * 2 
    return resultado
print(doble())
print(var)
print(resultado)