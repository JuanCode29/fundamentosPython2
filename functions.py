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