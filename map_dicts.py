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
print(list(map(lambda rectangulo: rectangulo['longitud'], rectangulos)))
print(list(map(lambda rectangulo: rectangulo['ancho'], rectangulos)))