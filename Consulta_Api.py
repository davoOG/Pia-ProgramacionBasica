import requests
import json
from FUNCIONES import Volver_Menu as Volver_Menu

def Consultar_Api():
    name = str(input("Ingrese el nombre del personaje: "))
    #Consulta la api buscando con el nombre proporcionado por el usuario
    try:
        url = f"https://swapi.dev/api/people/?search={name}"
        response = requests.get(url)
        datos_personaje = {}
        #Se comprueba que la consulta halla sido exitosa
        if response.status_code == 200:
            #Se guarda la informacion de la consulta en la variable data
            data=response.json()
            if data['count'] > 0:
                print(f"Se encontraron {data['count']} resultados: ")
                for personaje in data['results']:
                    #Se imprimen y se guardan los datos en distintas variables
                    print("--------------------------------")
                    print(f"Nombre : {personaje['name']}")
                    print(f"Altura: {personaje['height']} cm")
                    print(f"Peso: {personaje['mass']} kg")
                    print(f"Sexo: {personaje['gender']}")
                    print(f"Color de pelo: {personaje['hair_color']}")
                    print(f"Color de piel: {personaje['skin_color']}")
                    nombre = personaje['name']
                    altura = personaje['height']
                    peso = personaje['mass']
                    sexo = personaje['gender']
                    color_pelo = personaje['hair_color']
                    color_piel = personaje['skin_color']
                    #Se le pregunta al usuario si desea guardar la informacion
                    guardar = int(input("¿Desea guardar la informacion de esta consulta?\n1.Si\n2.No\n-"))
                    while guardar <1 or guardar >2:
                        print("ERROR: Opcion no valida")
                        guardar = int(input("¿Desea guardar la informacion de esta consulta?\n1.Si\n2.No\n-"))
                    #Si decide conservar la informacion los datos se guardan en el dic datos_personaje
                    if guardar == 1:
                        datos_personaje[nombre] = {
                            "nombre" : nombre,
                            "altura": altura, 
                            "peso": peso, 
                            "sexo": sexo, 
                            "color_pelo": color_pelo, 
                            "color_piel": color_piel
                            }
                        #Se manda a llamar a la funcion Guardar_Info y se le da datos_personaje[nombre] como dato de entrada
                        Guardar_Info(datos_personaje[nombre])
            else:
                print("No se encontraron resultados")   
                Volver_Menu() 
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud: {e}')
        Volver_Menu()


def Guardar_Info(datos_personajes):
    #Se establece el nombre del archivo que se va a usar
    nombre_archivo = "info.txt"
    #Se usa try y except para evitar errores a la hora de leer el archivo
    try:
        #Se abre el arhvio
        with open(nombre_archivo, 'a') as archivo:
            #Guardamos los datos en el archivo
            archivo.write(json.dumps(datos_personajes))
            archivo.write('\n')
        print(f"La informacion se guardo en '{nombre_archivo}")
        Volver_Menu()
    #Ayuda a mantener la integridad del programa al evitar fallos
    except Exception as e:
        print(f"Error al guardar la informacion: {e}")
        Volver_Menu()