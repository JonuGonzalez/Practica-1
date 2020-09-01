import cargar
import json
import re
registro = []
def inicio():
    print("Para Iniciar Presione 1")
    print("para salir presione 0")
    opcion = input()
    if opcion == "1":
        comandos()
    else:exit()

def comandos():
    print("Escribe un comando")
    instruccion = input()
    conversion = instruccion.lower()
    validar = 'cargar' in conversion
    if validar == True:
        comando = conversion.strip('cargar')
        archivo = comando.strip().split(', ')
        for file in archivo:
            registro = cargar(file)
    inicio()
    return registro

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
print(registro)

inicio()