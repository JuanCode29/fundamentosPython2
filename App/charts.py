import matplotlib.pyplot as plt
import numpy as np
# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 25, 15, 30, 20]

# Crear un gráfico de barras
plt.bar(categorias, valores)
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.show()
#------------------------------------
# Crear un gráfico de dispersión
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

plt.scatter(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')
plt.show()
#------------------------------------
# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

# Crear un gráfico de líneas
plt.plot(x, y, label='Datos de ejemplo')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Líneas')
plt.legend()
plt.show()

#------------------------------------
# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 25, 15, 30, 20]

# Crear un gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
plt.title('Gráfico de Pastel')
plt.show()

#-------------------------------
# Datos de ejemplo
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura y subtramas (en este caso, 2x1, dos filas y una columna)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6))

# Subtrama 1: Gráfico de seno
axes[0].plot(x, y1, label='sin(x)', color='blue')
axes[0].set_xlabel('X')
axes[0].set_ylabel('sin(x)')
axes[0].set_title('Gráfico de Seno')
axes[0].legend()

# Subtrama 2: Gráfico de coseno
axes[1].plot(x, y2, label='cos(x)', color='red')
axes[1].set_xlabel('X')
axes[1].set_ylabel('cos(x)')
axes[1].set_title('Gráfico de Coseno')
axes[1].legend()

# Ajustar el espacio entre subtramas
plt.tight_layout()

# Mostrar la figura
plt.show()