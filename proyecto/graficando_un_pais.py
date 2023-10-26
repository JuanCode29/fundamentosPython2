#IMPORTAMOS LIBRERÍA
import csv
import re
import matplotlib.pyplot as plt
def read_csv(path):
    with open(path, 'r') as archivo:
        lector = csv.reader(archivo, delimiter=',')
        data = []
        claves = next(lector)
        for fila in lector:
            iterable = zip(claves, fila)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def select_pais(pais):
        for paises in datos_por_paises:
            if paises['Country/Territory'] == pais:
                población_dict = {re.match(r'\d+', año).group(): int(poblacion) for año, poblacion in paises.items() if re.match(r'\d+', año)}
                return población_dict
        return None

def grafica_poblacion_pais(años, poblaciones, pais):
    plt.figure(figsize=(10, 6))
    plt.plot(años, poblaciones, color='royalblue', marker='o', linestyle='-')
    plt.xlabel('Año')
    plt.ylabel('Población')
    plt.title(f'Población de {pais} a lo largo de los años')
    plt.grid(True)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    datos_por_paises = read_csv('./data.csv')
    pais = input('Ingrese pais')
    datos_pais_seleccionado = select_pais(pais)
    
    if datos_pais_seleccionado is not None:
        años = list(datos_pais_seleccionado.keys())
        poblaciones = list(datos_pais_seleccionado.values())
        grafica_poblacion_pais(años, poblaciones, pais)
    else:
        print('País no encontrado en los datos CSV.')