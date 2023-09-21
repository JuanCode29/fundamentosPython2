#file = open('./miArchivo.txt')
#print(file.read())
'''print(file.readline())
print(file.readline())
print(file.readline())'''

'''for i in file:
    print(i)
file.close()'''

with open('./miArchivo.txt') as archivo:
    contenido = archivo.read()
print(contenido)

with open('./miArchivo.txt') as archivo:
    for line in archivo:
        print(line.strip())# strip() elimina espacios en blanco y saltos de línea al final de cada línea