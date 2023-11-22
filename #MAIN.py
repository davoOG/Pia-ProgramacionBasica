from Consulta_Api import Consultar_Api
from Excel import TXTaLista
from Graficas import Menu_Graficas

while True:
    print("--------------------------------")
    print("Programa para consultar info de \nPersonajes de STAR WARS:")
    print("--------------------------------")
    print("MENU:")
    print("1. Consultar API")
    print("2. Graficas")
    print("3. Excel")
    print("4. Salir")
    print("--------------------------------")
    
    opcion = int(input("Selecciona una opción (1-4): "))
    
    while opcion < 1 or opcion > 4 :
        print("Opción no valida. Por favor, selecciona una opcion válida")
        opcion = int(input("Selecciona una opción (1-4: )"))
    
    if opcion == 1:
        print("--------------------------------")
        print("CONSULTAR API")
        Consultar_Api()

    elif opcion == 2:
        print("--------------------------------")
        print("GRAFICAS")
        Menu_Graficas()

    elif opcion == 3:
        print("--------------------------------")
        print("EXCEL")
        TXTaLista(1)

    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break