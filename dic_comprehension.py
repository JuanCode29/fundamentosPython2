#nuevo_diccionario = {clave: valor for elemento in secuencia if condicion}
#SIN DICT COMPREHENSION
dict = {}
for i in range(1, 5):
    dict[i] = i*2
print(dict)