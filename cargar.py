import json
import main
def json(archivo):
    with open(archivo) as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        main.array.append([n, e, a, p])
    print(main.array)
    return main.array

