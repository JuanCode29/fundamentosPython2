# CREACIÓN DE FUNCIONES
def my_function():
    print("Hello from a function")
# LLAMAMOS LA FUNCCIÓN
my_function()

#FUNCION CON PARÁMETROS

def suma(a, b):
    result = a + b
    return result

print(suma(6, 7))

#SI SE DESCONOCE EL NÚMERO DE ARGUMENTOS (*args):

def  my_siblings(*name):
    print(f"Mi segundo hermano es: {name[2]}")

my_siblings('Juan', 'Jose', 'Nexar')


#ARGUMENTOS DE PALABRA CLAVE(**kwargs):

def funcion_con_kwargs(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

funcion_con_kwargs(Nombre = 'Juan', edad = 20)

#UTILIZANDO (*args y **kwargs)

def funcion_con_args_y_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs.items():
        print(kwarg)

funcion_con_args_y_kwargs(1, 2, 3, Nombre = 'Juan', edad = 30)

#PARÁMETRO PREDERTERMINADO:

def saludar(nombre, mensaje="¡Hola!"):
    print(mensaje, nombre)

saludar("Juan")  # Salida: ¡Hola! Juan
saludar("Ana", "¡Hola de nuevo!")  # Salida: ¡Hola de nuevo! Ana

#EJEMPLOS VARIOS

#1. CALCULAMOS EL ÁREA DE UN RECTANGULO(Usamos PARÁMETROS PREDERTIMINADOS):

def área_rectángulo(base = 4, altura = 10):
    return base * altura

area = área_rectángulo() #Utilizando valores predeterminados
print(area)

area_personalizada = área_rectángulo(20, 30)
print(area_personalizada)

#2. CALCULAMOS LA SUMA DE LOS "n" primeros números naturales:

def suma_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma = suma + i
        print(i)
    print("---")
    print(suma)

suma_numeros(6)

#2. Factorial de un número:

def factorial_num (n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial_num(n-1)

resultado = factorial_num(5)
print(resultado)

#3. Factorial con bucle for

def factorial_num(n):
    factorial = 1
    for i in range(1, n + 1):
        print(i, end=" ")  # Imprimir el valor de i seguido de un espacio en lugar de un salto de línea
        factorial *= i
    print()  # Imprimir una línea en blanco para separar la salida
    return factorial

resultado = factorial_num(5)
print("Factorial:", resultado)
