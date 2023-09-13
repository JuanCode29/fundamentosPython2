productos = [
    {'Nombre': 'Producto 1', 'Precio': 50},
    {'Nombre': 'Producto 2', 'Precio': 100},
    {'Nombre': 'Producto 3', 'Precio': 200}
]

def calcular_IGV(producto):
    producto['igv'] = producto['Precio'] * 0.18
    return producto

productos_final = list(map(calcular_IGV, productos))
print(productos_final)


#EJEMPLO 02 - LISTAS

numeros = [1, 2, 3, 4, 5, 6]
calcular_cuadrado = lambda n: n*n
print(list(map(calcular_cuadrado,numeros)))

#EJEMPLO 03 - DICCIONARIOS

rectangulos = [
    {'longitud': 5, 'ancho': 4},
    {'longitud': 3, 'ancho': 6},
    {'longitud': 7, 'ancho': 2}
]

def calcular_area(rectangulo):
    rectangulo['area'] = rectangulo['longitud'] * rectangulo['ancho']
    return rectangulo

print(list(map(calcular_area, rectangulos)))

# AL APLICAR la función calcular_area dentro de map(); modifica los diccionarios originales en la lista rectángulos.

print(rectangulos)

#Forma de imprimir solo las claves de los diccionarios.
print(list(map(lambda rectangulo: rectangulo['longitud'], rectangulos)))

#Forma de imprimir solo los valores de las palabras clave de los diccionarios.
print(list(map(lambda rectangulo: rectangulo['ancho'], rectangulos)))


#EJEMPLO 04: Para evitar cambiar el diccionario original, realizamos lo siguiente

rectangulos2 = [
    {'longitud': 5, 'ancho': 4},
    {'longitud': 3, 'ancho': 6},
    {'longitud': 7, 'ancho': 2}
]

# Definimos una función para calcular el área y crear un nuevo diccionario
def calcular_area2(rectangulo2):
    area = rectangulo2['longitud'] * rectangulo2['ancho']
    return {**rectangulo2, 'area': area}#** permite crear un nuevo diccionario y agregarle una nueva clave

#Utilizar una comprensión de lista para crear nuevos diccionarios con áreas

rectangulos_con_areas = [calcular_area2(dimension) for dimension in rectangulos2]

print(rectangulos_con_areas)

# Solo que en este caso ya no se utilizó map