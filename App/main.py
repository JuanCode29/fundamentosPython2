import importlib # Para recargar el módulo importado cuando éste sufrio algún cambio.
import utils #Importamos todo el módulo

# Actualizamos el módulo importado:
importlib.reload(utils)

# Consultamos los nombres de funciones (o nombres de variables) en el módulo:
print( dir(utils))

# Se observa lo siguiente:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'greeting', 'person1']

#Ejecutamos la variable:
print(utils.a)

# Llamamos a la funcción:
utils.greeting('Juan')

# Imprimimos el diccionario:
print(utils.person1)


#IMPORTAMOS SOLO PARTES DEL MODULO

#Importamos solo la funcción:

from utils import greeting
greeting('Pablo')

#Importamos solo el diccionario:

from utils import person1

print(person1)

print(list(filter(lambda persona: persona['age'] == 37, person1)))

#IMPORTAMOS LA FUNCIÓN OBTENER EDAD
import importlib
importlib.reload(utils)
from utils import obtener_edad

# Llamamos a la función para obtener la edad por nombre

name = input("Nombre de la persona que quiere obtener la edad: ")
age = obtener_edad(name)

if age is not None:
    print(f"La edad de {name} es: {age}")
else:
    print(f"No se encontró a {name} en la lista.")