print("A continuación se muestran tres archivos",)
import cargar
import re

print("Bienvenido Para Iniciar Con el Sistema Utilice el Comando Cargar")
instruccion = input()
conversion = instruccion.lower()
validar = 'cargar' in conversion
if validar == True:
    comando = conversion.strip('cargar')
    archivo = comando.strip().split(',')
    for file in archivo:
        cargar.cargar(file)
