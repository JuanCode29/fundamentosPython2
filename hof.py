#1.- FUNCIONES QUE TOMAN FUNCIONES COMO ARGUMENTO
lista_numeros = [1, 2, 3, 4, 5, 6]

def aplicar_funcion(funcion, lista):
    aplicando = [funcion(x) for x in lista]
    return aplicando

def cuadrado(x):
    return x*x

resultado = aplicar_funcion(cuadrado, lista_numeros)
print(resultado)

#2.- FUNCIONES QUE DEVUELVEN FUNCIONES

def crear_funcion_multiplicadora(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar

duplicar = crear_funcion_multiplicadora(2)

resultado = duplicar(5)
print(resultado)