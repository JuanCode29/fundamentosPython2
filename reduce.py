import functools
#Calculamos la sumatoria de los números en la lista:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Definimos la función suma

def suma(x, y):#x inicialmente va tomar el primer elemento de la lista y luego se convierte en acumulador.
    return x + y

#Obtenemos el resultado final:

resultado = functools.reduce(suma, numeros)
print(resultado)