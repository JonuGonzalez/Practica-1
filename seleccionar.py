def seleccionar(data, archivo):
    for entidad in data:
        entidadnombre = entidad['nombre']
        print(entidadnombre)
    array = data
    print(array)
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        array.append([n, e, a, p])
    return data