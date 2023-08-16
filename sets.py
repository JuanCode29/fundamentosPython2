#CREACIÓN DE UN CONJUNTO
myset = {1, 2, 3, 4}
print(myset)

myset =set((1, 2, 3, 4))#Otra forma de crear conjuntos
print(type(myset))

#el 1 y True se consideran un mismo valor
myset = {1, 2, 3, 4, True}
print(myset)

#No permite duplicados:
myset = {1,2,3,4,1,2}
print(myset)

#LONGITUD DE UN CONJUNTO
myset = {1,2,3,4,1,2}
numero_elementos = len(myset)#NO CONSIDERA A LOS DUPLICADOS
print(numero_elementos)