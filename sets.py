#CREACIÓN DE UN CONJUNTO
myset = {1, 2, 3, 4}
print(myset)

myset =set((1, 2, 3, 4))#Otra forma de crear conjuntos
print(type(myset))

#el 1 y True se consideran un mismo valor
myset = {1, 2, 3, 4, True}
print(myset)

#No permite duplicados:
myset = {1, 2, 3, 4, 1, 2}
print(myset)

#LONGITUD DE UN CONJUNTO
myset = {1,2,3,4,1,2}
numero_elementos = len(myset)#NO CONSIDERA A LOS DUPLICADOS
print(numero_elementos)

#RECORRIDO DE  LOS LEMENTOS DE UN CONJUNTO
myset = {1, 2, 3, 4}
for element in myset:
    print(element)

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
for city in mycity:
    if city == "Rioja":
        print(f"La ciudad de {city} si esta en la lista")
    else:
        continue
        print(f"La ciudad de {city} No esta en la lista")

#AGREGAR ELEMENTOS AL CONJUNTO:
#1. método .add(elemento)
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity.add("Yurimaguas")
print(mycity)

#2. método update(): Permite agregar elementos de un conjunto a otro o tambien puede ser cualquier objeto iterable (tuplas, listas, diccionarios, etc.)..
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas"}
mycity.update(mycity2)
print(mycity)

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mylist = ["Tocache", "Lamas"]
mycity.update(mylist)
print(mycity)

#ELIMINAR ELEMENTOS DE UN CONJUNTO:
#Para eliminar un elemento de un conjunto, utilice el método remove()o el discard().

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity.remove("Tarapoto")#Si el elemento a eliminar NO EXISTE, se genera un ERROR
print(mycity)

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity.discard("Tarapoto")#Si el elemento a eliminar NO EXISTE, NO genera ERROR
print(mycity)