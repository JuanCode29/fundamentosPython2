#CREACIÓN DE UN CONJUNTO
myset = {1, 2, 3, 4}
print(myset)

myset =set((1, 2, 3, 4))#Otra forma de crear conjuntos
print(type(myset))

myset = set("HOLA")#cREAMOS UN CONJUNTO A PARTIR DE UNA CADENA
print(myset)

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

#Método .pop(): Este método elimina cualquier elemento de manera aleatoria y su valor de retorno es el elemento eliminado

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
elemento_eliminado = mycity.pop()
print(elemento_eliminado)
print(mycity)

#VACIAR Y ELIMINAR  CONJUNTO:
#1. Vaciar conjunto:
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity.clear()
print(mycity)

#2. Eliminar conjunto
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
del mycity
print(mycity)#Resultado ERROR porque el conjunto ya no existe.

# UNION DE CONJUNTOS
#1. Método .union():  devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas"}
union_city = mycity.union(mycity2)
print(union_city)

#2. El método update() inserta los elementos en mycity2 en mycity:
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas"}
mycity.update(mycity2)
print(mycity)

#3. Usando "|"

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas"}

print(mycity | mycity2)

#INTERSECCION DE CONJUNTOS:
#1. Método intersection_update(): Mantiene solo los elementos que están presentes en ambos conjuntos

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}
mycity.intersection_update(mycity2)
print(mycity)

#2. Método intersection(): devolverá un nuevo conjunto, que solo contiene los elementos que están presentes en ambos conjuntos.

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}
interseccion = mycity.intersection(mycity2)
print(interseccion)

# Usando "&"

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}

print(mycity & mycity2)

#DIFERENCIA SIMÉTRICA:
#1.El método symmetric_difference_update() mantendrá solo los elementos que NO están presentes en ambos conjuntos.
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}
mycity.symmetric_difference_update(mycity2)
print(mycity)

#2. El método symmetric_difference() devolverá un nuevo conjunto, que contiene solo los elementos que NO están presentes en ambos conjuntos.
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}
mycity_diferente = mycity.symmetric_difference(mycity2)
print(mycity_diferente)

#3. Usando "^":

mycity = {"Rioja", "Moyobamba", "Tarapoto"}
mycity2 = {"Tocache", "Lamas", "Rioja", "Tarapoto"}

print(mycity ^ mycity2)

#COPIAR CONJUNTO:
mycity = {"Rioja", "Moyobamba", "Tarapoto"}
copy_city = mycity.copy()
print(copy_city)

#DIFERENCIA DE CONJUNTOS:
#1. Método .difference(): Devuelve un conjunto que contiene los elementos que solo existen en el conjunto x y no en el conjunto y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#2. Método .difference_update():Eliminar los elementos que existen en ambos conjuntos.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

y.difference_update(x)
print(y)

#3. Usando "-"

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x -y )

#OTROS MÉTODOS:
#1. isdisjoint():Devuelve True si no hay elementos en el conjunto x presentes en el conjunto y. Lo contrario devuelve False.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#2. Set issubset():Devuelve True si todos los elementos del conjunto x están presentes en el conjunto y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#3.Método issuperset(): devuelve True si todos los elementos del conjunto especificado existen en el conjunto original; de lo contrario, devuelve False.
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
