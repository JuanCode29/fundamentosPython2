import csv
import matplotlib.pyplot as plt

# Importa tus datos
from graficando_un_pais import read_csv

data = read_csv('./data.csv')

# Solicitar al usuario que ingrese el continente
continente_deseado = input("Ingresa el nombre del continente que deseas visualizar: ")

# Filtrar los datos para el continente deseado
datos_continente = [dato for dato in data if dato['Continent'] == continente_deseado]

# Preparar datos para el gráfico de pastel
paises = []
porcentajes = []

for dato in datos_continente:
    pais = dato['Country/Territory']
    porcentaje = dato['World Population Percentage']
    if float(porcentaje) < 1:
        pais = 'Otros'
    paises.append(pais)
    porcentajes.append(porcentaje)

# Crear un gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(porcentajes, labels=paises, autopct='%1.1f%%', startangle=140)
plt.title(f'Distribución de la población en {continente_deseado}')
plt.axis('equal')
plt.show()



