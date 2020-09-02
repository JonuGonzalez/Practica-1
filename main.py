import cargar
import json
import re
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
    elif opcion == "3":
        maximo()
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

def seleccionar(data):
    for entidad in data:
        n = entidad['nombre']
        e = entidad['edad']
        a = entidad['activo']
        p = entidad['promedio']
        array.append([n, e, a, p])
    print(array)
    return data

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
            print("La edad mas alta es: ")
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

def prueba():
    print(array)

menu()