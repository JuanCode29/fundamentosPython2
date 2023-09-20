#CAPTURAMOS EL ERROR
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

print('hola')
try:
    assert 5 < 4, 'Tiene que ser menor a 4'
except AssertionError as error:
    print(error)

print('Hola2')

try:
    x = 20
    if x > 15:
        raise ValueError('x no puede ser menor a 15')
except ValueError as error:
    print(error)
print('Hola3')