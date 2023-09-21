#CREAMOS y ESCRIBIMOS UN ARCHIVO
#'x' (Modo de creación exclusiva): Este modo se utiliza para crear un archivo nuevo y, si ya existe un archivo con el mismo nombre, se generará un error (FileExistsError). Es útil cuando deseas asegurarte de que el archivo no exista previamente antes de crearlo.#

with open('archivo_nuevo.txt', 'x') as archivo:
    archivo.write('Este es un nuevo archivo.')

#'a' (Modo de agregado): En este modo, el archivo se abre para escritura, pero si el archivo ya existe, el nuevo contenido se agrega al final del archivo en lugar de sobrescribirlo. Si el nuevo texto queremos agregarlo a la siguiente línea utilizamos '\n'#

with open('archivo_nuevo.txt', 'a') as archivo:
    archivo.write("\nEste contenido se agrega al final del archivo.")

#'w' (Modo de escritura): Este modo se utiliza para abrir un archivo en modo escritura. Si el archivo ya existe, su contenido se sobrescribirá. Si no existe, se creará un archivo nuevo.#

with open('miArchivo2.txt', 'w') as archivo:
    archivo.write("Este contenido sobrescribirá el contenido anterior.")

# MODO LECTURA Y ESCRITURA

with open('miArchivo.txt', 'r+') as archivo:
    contenido = archivo.read()# Leer contenido existente.
    print('Contenido actual del archivo:')
    print(contenido)

    # Escribir contenido adicional al final del archivo
    archivo.write("\nEste es contenido adicional.")

    # Regresar al inicio del archivo para leer desde el principio

    archivo.seek(0)

    #Leer el contenido modificado
    nuevo_contenido = archivo.read()
    print("Contenido modificado del archivo:")
    print(nuevo_contenido)

#w+: Me permite no solo escribir, si no tambien leer

with open('Archivo.txt', 'w+') as archivo:
    # Escribir contenido en el archivo
    archivo.write('Este es un nuevo archivo2')
    # Regresar al inicio del archivo para leer desde el principio
    archivo.seek(0)

    # Leer el contenido recién escrito
    contenido = archivo.read(6)#Lee solo 6 caracteres. Pra que lo lea todo lo dejamos vacio read()
    print(contenido)

#x+:se utiliza para abrir un archivo en modo de creación exclusiva, lo que significa que se crea un nuevo archivo si no existe, pero genera un error si el archivo ya existe. Además, el modo 'x+' permite tanto la lectura como la escritura en el archivo. 

with open('archivo_nuevo2.txt', 'x+') as archivo:
    # Escribir contenido en el archivo
    archivo.write("Este es un nuevo archivo.")

    # Regresar al inicio del archivo para leer desde el principio
    archivo.seek(0)

    # Leer el contenido recién escrito
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# a+: El modo 'a+' en la función open se utiliza para abrir un archivo en modo de agregado y lectura.

# Abrir el archivo en modo 'a+' para agregar y leer
with open('miArchivo.txt', 'a+') as archivo:
    # Agregar líneas al final
    archivo.write("\nLínea 6")
    archivo.write("\nLínea 7")

    # Regresar al inicio del archivo para leer desde el principio
    archivo.seek(0)

    # Leer y mostrar el contenido
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)