import utils #Importamos todo el módulo

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