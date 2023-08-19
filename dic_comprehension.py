#nuevo_diccionario = {clave: valor for elemento in secuencia if condicion}
#SIN DICT COMPREHENSION

dict = {}
for i in range(1, 5):
    dict[i] = i*2
print(dict)

#con dict comprehension

dict = {i:i*2 for i in range(1, 5)}
print(dict)

#ejemplo 01: Generamos población aleatoria para ciudades:
import random
paises = ['Per', 'Col', 'Bol']
poblacion = {}

for pais in paises:
    poblacion[pais] = random.randint(1000, 2000)
print(poblacion)

#con dict comprehension:

poblacion = {pais: random.randint(1000, 2000) for pais in paises}
print(poblacion)

#ejemplo 02:

names = ['Juan', 'Pablo', 'Jose']
ages = [38, 37, 28]

names_ages = { name: age for name, age in zip(names, ages)}
print(names_ages)

#Ejemplo 03:
import random
paises = ['Per', 'Col', 'Bol']
poblacion_v1 = { pais: random.randint(1000, 2000) for pais in paises}
print(poblacion_v1)

poblacion_v2 = {pais: poblacion for pais, poblacion in poblacion_v1.items() if poblacion > 1700}
print(poblacion_v2)

#Ejemplo 04:

texto = 'Hola, soy Juan Pablo'
unique = {v: v.upper() for v in texto if v in 'aeiou'}
print(unique)

frecuencia = {vocal: texto.count(vocal) for vocal in texto if vocal in 'aeiou'}
print(frecuencia)