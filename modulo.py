# MODULO sys
#Es una lista que contiene las rutas de búsqueda utilizadas por Python para buscar módulos y paquetes importados. Son las posibles rutas donde python buscará los módulos a importar.
import sys
print(sys.path)

#Modulo re:Implementa expresiones regulares para buscar y manipular patrones de texto en cadenas.

import re
texto = "Mi numeros de telefono es 901452674 y tengo 38 años y mi número de la suerte es 25"
resultado = re.findall('[0-9]+', texto)
print(resultado)

#MODULO time: Proporciona funciones para trabajar con el tiempo y la fecha. Puedes utilizarlo para medir el tiempo de ejecución de tu programa, crear retardos, formatear fechas y más. 
import time
hora_actual = time.time() #FORMATO UNIX
print(hora_actual)

local = time.localtime()
resultado = time.asctime(local)
print(resultado)

#Módulo collectios: 
import collections
lista = [1, 2, 3, 1, 2, 4, 5, 4]
counter = collections.Counter(lista) #Muesta un diccionario donde la clave es cada elemento y como valor las veces que se repite en la lista dicho elmento.
print(counter)