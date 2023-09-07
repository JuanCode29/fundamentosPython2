numeros = [1, 2, 3, 4, 5]
cuadrado = []
for i in numeros:
    cuadrado.append(i*i)
print(cuadrado)

#CON LA FUNCION map()
numeros = [1, 2, 3, 4, 5]
cuadrado_2 = list(map(lambda i: i * i, numeros))
print(cuadrado_2)

#EJEMPLO
numeros = [1, 2, 3, 4, 5]
numeros_2 = [1, 2, 3]

resultado = list(map(lambda x, y: x + y, numeros, numeros_2))
print(numeros)
print(numeros_2)
print(resultado)