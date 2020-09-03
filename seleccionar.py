def seleccionar(data):
    for entidad in data:
        entidadnombre = entidad['nombre']
        print(entidadnombre)
    luz = data

    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        luz.append([n, e, a, p])
    print(luz)
    return data

todo = '*' in atributos
            if todo == True:
                n = entidad['nombre']
                e = entidad['edad']
                a = entidad['activo']
                p = entidad['promedio']
                s.append([n, e, a, p])
                print(s)