#nuevo_diccionario = {clave: valor for elemento in secuencia if condicion}
#SIN DICT COMPREHENSION
dict = {}
for i in range(1, 5):
    dict[i] = i*2
print(dict)

#con dict comprehension

dict = {i:i*2 for i in range(1, 5)}
print(dict)

#Generamos población aleatoria para ciudades:
import random
paises = ['Per', 'Col', 'Bol']
poblacion = {}

for pais in paises:
    poblacion[pais] = random.randint(1000, 2000)
print(poblacion)

#con dict comprehension:

poblacion = {pais: random.randint(1000, 2000) for pais in paises}
print(poblacion)