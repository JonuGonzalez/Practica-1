print("A continuación se muestran tres archivos",)
import cargar
import re

print("Bienvenido Para Iniciar Con el Sistema Utilice el Comando Cargar")
comando = input()
conversion = comando.lower()
validar = 'archivo1' in conversion
if validar == True:
    print(validar)
    print(conversion)
    archivo = conversion
    cargar.cargar(archivo)