# CACLULAMOS EL ÁREA DE LOS RECTANGULOS y lo agregamos como nuevo atributo sin modificar los diccionarios originales.
rectangulos = [
    {'longitud': 5, 'ancho': 4},
    {'longitud': 3, 'ancho': 6},
    {'longitud': 7, 'ancho': 2}
]

# Definimos una funcion  para calcular el área y crear un nuevo diccionario

def calcular_area(rectangulo):
    new_rectangulo = rectangulo.copy()# Crear una copia del diccionario original
    new_rectangulo['area'] = new_rectangulo['longitud'] * new_rectangulo['ancho']
    return new_rectangulo

# Utilizar map para aplicar la función calcular_area a cada rectángulo
rangulos_con_areas = list(map(calcular_area, rectangulos))

# Imprimir la lista de rectángulos con áreas calculadas
print(rangulos_con_areas)

# La lista original 'rectangulos' no se modifica
print(rectangulos)
