# Ejemplo 01:
cuadrado = lambda x : x**2
resultado = cuadrado(5)
print(resultado)

#Ejemplo 02:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#Ejemplo 03:
full_name = lambda name, last_name: f'Mi nombres es: {name.title()} {last_name.title()}'

print(full_name('Juan', 'Quispe Molina'))