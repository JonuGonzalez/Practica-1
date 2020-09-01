import json

def cargar(archivo):
    with open(archivo+'.json') as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    print(data)
    for entidad in data:
        entidadnombre = entidad['nombre']
        print(entidadnombre)
    array = data
    print(array)
    return data

