# Error ZeroDivisionError:
#print(10/0) # ZeroDivisionError: division by zero

# Error SyntaxError:
#print('Hola, Mundo' # SyntaxError: '(' was never closed

# NameError:
#print(variable_inexistente)#NameError: name 'variable_inexistente' is not defined

# Uso de assert para verificaciones:se utiliza para verificar que una condición sea verdadera. Si la condición es falsa, se lanza una excepción AssertionError.
print('Hola')
suma = lambda x, y: x + y
assert suma(4, 6) == 9, "La suma es incorrecta" # AssertionError: La suma es incorrecta
print('Hola2')