import csv
import re
import matplotlib.pyplot as plt

class PopulationData:
    def __init__(self, data_path):
        # Constructor de la clase, carga los datos del archivo CSV al crear una instancia
        self.data = self.read_csv(data_path)

    def read_csv(self, path):
        try:
            # Lee los datos del archivo CSV y los almacena en una lista de diccionarios
            with open(path, 'r') as archivo:
                lector = csv.reader(archivo, delimiter=',')
                data = []
                claves = next(lector)
                for fila in lector:
                    iterable = zip(claves, fila)
                    country_dict = {key: value for key, value in iterable}
                    data.append(country_dict)
                return data
        except FileNotFoundError:
            print(f"Error: El archivo '{path}' no se encontró.")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    def select_country_data(self, country_name):
        # Busca los datos del país especificado en los datos cargados
        for paises in self.data:
            if paises['Country/Territory'] == country_name:
                # Extrae los datos de población para el país seleccionado
                población_dict = {re.match(r'\d+', año).group(): int(poblacion) for año, poblacion in paises.items() if re.match(r'\d+', año)}
                return población_dict
        return None

    def plot_population(self, country_name):
        datos_pais_seleccionado = self.select_country_data(country_name)
        
        if datos_pais_seleccionado is not None:
            # Prepara los datos para el gráfico
            años = list(datos_pais_seleccionado.keys())
            poblaciones = list(datos_pais_seleccionado.values())

            # Crea y muestra el gráfico de población
            plt.figure(figsize=(10, 6))
            plt.plot(años, poblaciones, color='royalblue', marker='o', linestyle='-')
            plt.xlabel('Año')
            plt.ylabel('Población')
            plt.title(f'Población de {country_name} a lo largo de los años')
            plt.grid(True)

            # Escala automática para números grandes
            max_poblacion = max(poblaciones)
            if max_poblacion > 1000000:
                plt.ticklabel_format(axis='y', style='sci', scilimits=(6, 6))

            # Mostrar el gráfico
            plt.tight_layout()
            plt.show()
        else:
            print(f'País {country_name} no encontrado en los datos CSV.')

if __name__ == '__main__':
    # Creación de una instancia de la clase PopulationData
    population_data = PopulationData('./data.csv')

    # Entrada del usuario para seleccionar un país y generar el gráfico
    country = input('Ingrese país: ')
    population_data.plot_population(country)
