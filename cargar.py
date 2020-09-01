import json

def cargar(archivo):
    with open(archivo+'.json') as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    array = []
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        array.append([n,e,a,p])
    print(array)
    return array

