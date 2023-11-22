import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode
from Excel import TXTaLista as TXTaLista

def Menu_Graficas():
    print("--------------------------------")
    print("DATOS ESTADISTICOS")
    print("1. Distribucion de Generos")
    print("2. Media de alturas")
    print("3.Grafica de linea con las edades")
    print("--------------------------------")
    opcion = int(input("Seleccione una opcion: "))
    while opcion < 1 or opcion > 3:
        print("ERROR: Opcion no valida")
        opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        PASTEL()
    elif opcion == 2:
        BARRAS()
    else:
        LINEA()

def PASTEL():
    datos = TXTaLista(2)
    # Contar la cantidad de hombres y mujeres
    cantidad_hombres = sum(personaje["sexo"] == "male" for personaje in datos)
    cantidad_mujeres = sum(personaje["sexo"] == "female" for personaje in datos)
    # Etiquetas y datos para la gráfica de pastel
    etiquetas = ['Hombres', 'Mujeres']
    datos = [cantidad_hombres, cantidad_mujeres]
    # Crear la gráfica de pastel
    plt.pie(datos, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Hombres y Mujeres')
    plt.show()

def BARRAS():
    datos = TXTaLista(2)
    # Extraer alturas de la lista de diccionarios
    alturas = [float(personaje["altura"]) for personaje in datos]
    # Calcular la media de alturas
    media_alturas = np.mean(alturas)
    # Definir los rangos de 10 unidades
    rangos = np.arange(150, 210, 10)
    # Crear un histograma de alturas por rangos
    plt.hist(alturas, bins=rangos, edgecolor='black', linewidth=1.2, alpha=0.7)
    # Agregar línea vertical para la media
    plt.axvline(media_alturas, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media_alturas:.2f}')
    # Ajustes de la gráfica
    plt.title('Distribución de Alturas por Rangos de 10 unidades')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Número de Personas')
    plt.xticks(rangos)
    plt.legend()  # Agregar la leyenda
    # Mostrar la gráfica
    plt.show()

def LINEA():
    datos = TXTaLista(2)
    # Extraer pesos de la lista de diccionarios
    pesos = [personaje["peso"] for personaje in datos]
    # Calcular la moda de los pesos
    moda_result = np.unique(pesos, return_counts=True)
    moda_indices = np.argmax(moda_result[1])  # Índice del valor más frecuente
    moda_pesos = moda_result[0][moda_indices]    # Crear una gráfica de línea con los pesos
    plt.plot(pesos, marker='o', linestyle='-', color='blue', label='Pesos')
    # Agregar línea vertical para la moda
    plt.axhline(moda_pesos, color='red', linestyle='dashed', linewidth=2, label=f'Moda: {moda_pesos}')
    # Ajustes de la gráfica
    plt.title('Pesos de Personas')
    plt.xlabel('Índice de Personas')
    plt.ylabel('Peso')
    plt.legend()  # Agregar la leyenda
    # Mostrar la gráfica
    plt.show()