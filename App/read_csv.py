import csv
# Abre el archivo CSV en modo lectura
def read_csv(ruta_file):
    with open(ruta_file, mode='r') as csvfile:
        lector_csv = csv.reader(csvfile, delimiter=',')
        data = []
        # Lee la primera fila como las claves
        claves = next(lector_csv)
        for fila in lector_csv:
            # Crea un diccionario utilizando las claves y los valores de la fila actual
            iterable = zip(claves, fila)
            country_dict = {key: value for key, value in  iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    resultado = read_csv('./data.csv')
    print(resultado[0])
