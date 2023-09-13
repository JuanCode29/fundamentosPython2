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
