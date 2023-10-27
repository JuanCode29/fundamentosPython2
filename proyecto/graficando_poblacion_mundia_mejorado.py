import csv
import matplotlib.pyplot as plt

# Importa tus datos
from graficando_un_pais import read_csv

# Función para obtener datos por continente
def obtener_datos_por_continente(datos, continente):
    # Filtra los datos según el continente deseado
    return [dato for dato in datos if dato['Continent'] == continente]

# Función para crear y mostrar un gráfico de pastel
def crear_grafico_pastel(paises, porcentajes, titulo):
    # Crea una figura de Matplotlib con un tamaño específico
    plt.figure(figsize=(8, 8))
    # Crea el gráfico de pastel con etiquetas, porcentajes y ángulo de inicio
    plt.pie(porcentajes, labels=paises, autopct='%1.1f%%', startangle=140)
    # Agrega un título al gráfico
    plt.title(titulo)
    # Hace que el gráfico sea un círculo perfecto
    plt.axis('equal')
    # Muestra el gráfico
    plt.show()

# Función principal del programa
def main():
    # Cargar datos desde un archivo CSV
    data = read_csv('./data.csv')

    # Solicitar al usuario que ingrese el continente de interés
    continente_deseado = input("Ingresa el nombre del continente que deseas visualizar: ")

    # Validar si el continente ingresado existe en los datos
    datos_continente = obtener_datos_por_continente(data, continente_deseado)
    if not datos_continente:
        print(f"No se encontraron datos para el continente '{continente_deseado}'.")
        return  # Sale del programa si no se encontraron datos

    # Preparar datos para el gráfico de pastel
    paises = [dato['Country/Territory'] for dato in datos_continente]
    porcentajes = [float(dato['World Population Percentage']) for dato in datos_continente]

    # Crear y mostrar el gráfico de pastel
    titulo = f'Distribución de la población en {continente_deseado}'
    crear_grafico_pastel(paises, porcentajes, titulo)

# Ejecuta la función principal si este script se ejecuta directamente
if __name__ == "__main__":
    main()
