#Crear una lista de cuadrados de números pares:

#1. SIN COMPREHENSION:

for x in range(1, 10):
    if x % 2  == 0:
        print(x,"\t",x**2)

#2. UTILIZANDO COMPREHENSION:

pares_cuadrados = [x**2 for x in range(1, 10) if x % 2 == 0]

print(pares_cuadrados)

for elemento in pares_cuadrados:
    print(elemento)