import json
import webbrowser
array = []
edad = []
promedio = []
def menu():
    print("")
    print("Selecciona el comando que deseas utilizar")
    print("1. Cargar")
    print("2. Seleccionar")
    print("3. Maximo")
    print("4. Minimo")
    print("5. Suma")
    print("6. Cuenta")
    print("7. Reportar")
    print("0. Salir")
    opcion = input('Escribe el numero de opcion que desees  ')
    if opcion == "1":
        analisiscargar()
    elif opcion == "2":
        seleccionar()
    elif opcion == "3":
        maximo()
    elif opcion == "4":
        minimo()
    elif opcion == "5":
        suma()
    elif opcion == "6":
        cuenta()
    elif opcion == "7":
        reportar()
        menu()
    elif opcion == "0":
        exit()

def analisiscargar():
    print("Escribe el comando Cargar")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'cargar' in conversion
    if validar == True:
        comando = conversion.lstrip('cargar')
        archivo = comando.strip().split(', ')
        for file in archivo:
            registro = cargar(file)
    else: print("No utilizaste el comando Cargar")
    menu()
    return registro

def cargar(archivo):
    with open(archivo) as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    for entidad in data:
        array.append(entidad)
    print(array)
    return array

def seleccionar():
    print("Escribe el comando Seleccionar")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'seleccionar' in conversion
    if validar == True:
        comando = conversion.lstrip('seleccionar ')
        atributos = comando.strip().split(', ')
        s=[]
        print(atributos)
        for entidad in array:
            nombre = 'mbre' in atributos
            edad = 'edad' in atributos
            activo = 'activo' in atributos
            promedio = 'promedio' in atributos
            if nombre == True:
                n = entidad['nombre']
                s.append(n)
                print(s)

                if edad == True:
                    e = entidad['edad']
                    s.append(e)

                    if activo == True:
                        a = entidad['activo']
                        s.append(a)

                        if promedio == True:
                            p = entidad['promedio']
                            s.append(p)
                            todo = '*' in atributos
                            if todo == True:
                                n = entidad['nombre']
                                e = entidad['edad']
                                a = entidad['activo']
                                p = entidad['promedio']
                                s.append([n, e, a, p])
                            print(s)

def maximo():
    print("Escribe el comando Maximo")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'maximo' in conversion
    if validar == True:
        comando = conversion.lstrip('maximo ')
        if comando == "edad":
            edad = []
            for entidad in array:
                e = entidad['edad']
                edad.append([e])
            print(edad)
            print("La edad mayor es: ")
            print(max(edad))
        elif comando == "promedio":
            promedio = []
            for entidad in array:
                p = entidad['promedio']
                promedio.append([p])
            print(promedio)
            print("El promedio mas alto es: ")
            print(max(promedio))
        else:print("Comando Invalido")
    else: print("No utilizaste el comando Maximo")
    menu()

def minimo():
    print("Escribe el comando Minimo")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'minimo' in conversion
    if validar == True:
        comando = conversion.lstrip('minimo ')
        if comando == "edad":
            edad = []
            for entidad in array:
                e = entidad['edad']
                edad.append([e])
            print(edad)
            print("La edad menor es: ")
            print(min(edad))
        elif comando == "promedio":
            promedio = []
            for entidad in array:
                p = entidad['promedio']
                promedio.append([p])
            print(promedio)
            print("El promedio mas bajo es: ")
            print(min(promedio))
        else:print("Comando Invalido")
    else: print("No utilizaste el comando Minimo")
    menu()

def suma():
    print("Escribe el comando Suma")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'suma' in conversion
    if validar == True:
        comando = conversion.lstrip('suma ')
        if comando == "edad":
            edad = []
            for entidad in array:
                e = entidad['edad']
                edad.append(e)
            print(edad)
            print("La suma de las edades es: ")
            print(sum(edad))
        elif comando == "promedio":
            promedio = []
            for entidad in array:
                p = entidad['promedio']
                promedio.append(p)
            print(promedio)
            print("La suma de los promedios es: ")
            print(sum(promedio))
        else:print("Comando Invalido")
    else: print("No utilizaste el comando Suma")
    menu()

def cuenta():
    print("Escribe el comando Cuenta")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'cuenta' in conversion
    if validar == True:
        cantidad = len(array)
        print(cantidad)
    else: print("No utilizaste el comando Cuenta")
    menu()

def reportar():
    print("Escribe el comando Reportar")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'reportar' in conversion
    if validar == True:
        comando = conversion.lstrip('reportar ')

    htmFile = open("reporte.html", "w")
    htmFile.write("""<!DOCTYPE HTML PUBLIC"

    <html>

    <head>
        <title>REPORTE</title>
     <meta charset="utf-5">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="../../../../vendors/css/vendor.bundle.base.css">
  <link rel="stylesheet" href="../../../../vendors/css/vendor.bundle.addons.css">

    <style type="text/css">
            body{
                background-color: #474D5A;
            }
            table tr:nth-child(even) {
  background-color: #eee;
}
table tr:nth-child(odd) {
  background-color: #fff;
}
table th {
  color: white;
  background-color: black;
}
            div#reporte {
                width: 60%;
                height: 98%;
                border:solid black;	
                background-color: #B1B7C4;
                margin: 20%;
                margin-top: 0;
                border-radius: 50px;
            }
            div#titulo{
                background-color: black;
                border:solid black;
                border-radius: 50px;
                height:10%;
            }
            h1{
                font-family: arial,helvetica;
                color: white;
            }
            h6{
                font-family: arial,helvetica;
                color: black;
            }
            h5{
                font-family: arial,helvetica;
                color: black;
            }
        </style>
    </head>
    <body>
        <div id="reporte">
            <div id="titulo">
                <center>
                    <h1>Reporte  Registros Seleccionados</h1>
                </center>
            </div>
            <center>            
  <table class="table table-hover">
    <thead>
      <tr>
       <th>nombre</th>
        <th>edad</th>
        <th>activo</th>
        <th>saldo</th>
      </tr>
    </thead>

    """)
    i=int(comando)
    p = array[0:i]
    contenido = ""
    for i in p:
            contenido += (" <tbody>"
                          "<td>" + i['nombre'] + "</td>"
                                                 "<td>" + str(i['edad']) + "</td>"
                                                                           "<td>" + str(i['activo']) + "</td>"
                                                                                                       "<td>" + str(
                i['promedio']) + "</td>"
                              "</tbody>")

    htmFile.write(contenido)

    htmFile.write("""

    </table>
    <h6>
                    Jonathan Ulises González Rodríguez
                </h6>
    </div>
    </body>
    </html>""")

    htmFile.close
    webbrowser.open_new_tab('reporte.html')

def prueba(data):
    luz = data
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        luz.append([n, e, a, p])
    print(luz)
    return data
menu()