#FILTRAMOS NUMEROS PARES
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_pares = list(filter(lambda i: i % 2 == 0, numeros))
print(numeros_pares)

# FILTRAMOS EN UNA LISTA DE DICCIONARIOS
personas = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'Ana', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 17},
    {'nombre': 'María', 'edad': 22},
    {'nombre': 'Luis', 'edad': 19}
]

#filtrar las personas mayores de 18 años

personas_mayores_18años = list(filter(lambda persona: persona['edad'] >= 18, personas))
print(personas_mayores_18años)