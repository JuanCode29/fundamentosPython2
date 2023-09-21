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