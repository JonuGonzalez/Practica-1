import cargar
import json
import re
array = []
def inicio():
    print("Para Escribir un Comando Presione 1")
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
    with open(archivo) as file:
        data = json.load(file)
        print("Archivo Cargado Correctamente")
    file.close()
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        array.append([n, e, a, p])
    print(array)
    return array
inicio()