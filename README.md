### Manual de usuario
Aplicacion SimpleSQL en lenguaje Python
- Todos los comandos necesarios para el uso de esta aplicacion se encuentra en un solo archivo el cual es main.py.
- Adicionalmente debe contar con archivos .json los cuales deben estar localizados en la carpeta en la que se encuentra el main.py
####Contenido
                
+ Menu
+ Archivos json
+ Comandos
    + Cargar
    + Seleccionar
    + Minimo
	+ Maximo
	+ Suma
	+ Contar
	+ Reportar
	+ Salir

####Menu
Al iniciar el main.py se presentara el siguiente menu

Selecciona el comando que deseas utilizar
1. Cargar
2. Seleccionar
3. Maximo
4. Minimo
5. Suma
6. Cuenta
7. Reportar
0. Salir

Escribe el numero de opcion que desees

Unicamente debe ingresar el numero de la opcion que desea efectuar.
Cada vez que selecciona una opcion el programa se enfoca en algoritmos especificos para cada opcion.

####Archivos Json
Este programa trabaja con archivos .json los archivos JSON (JavaScript Object Notation - Notación de Objetos de JavaScript) es un formato ligero de intercambio de datos. Leerlo y escribirlo es simple para humanos, mientras que para las máquinas es simple interpretarlo y generarlo.

Lo que hace este programa es tomar los archivos json obtener la informacion que contienen y manipularla por medio de los comandos.

####Comandos
Los comandos son imitaciones o similares a la sintaxis que se utiliza en un lenguaje sql, aunque este programa no utiliza lenguaje SQL ya que toda la progamacion esta en lenguaje Python.

Esta aplicacion cuenta con 8 comandos los cuales se detallan acontinuación.

#####Cargar
- El comando cargar permite ingresar archivos .json para utilizarlos en los demás comandos. Puede cargar tantos archivos .json como lo desee.

- La intruccion de este comando es la siguiente:

- Cargar archivo1.json

#####Seleccionar
- El comando seleccionar permite escojer atributos especificos de un arrelgo que contiene la informacion de los archivos .json cargados.

- La intruccion de este comando es la siguiente:

- Seleccionar nombre

#####Maximo
- El comando maximo permite determinar el mayor valor entre dos tipos de atributos: Edad y Promedio.

- La intruccion de este comando es la siguiente:

- maximo edad ó maximo promedio

#####Minimo
- El comando minimo permite determinar el menor valor entre dos tipos de atributos: Edad y Promedio.

- La intruccion de este comando es la siguiente:

- minimo edad ó minimo promedio

#####Suma
- El comando suma permite hacer una adicion entre dos tipos de atributos: Edad y Promedio.

- La intruccion de este comando es la siguiente:

- suma edad ó suma promedio

#####Cuenta
- El comando Cuenta permite mostrar la cantidad de registos que se encuentran en memoria los cuales pertenecen a los archivos .json cargado.

- La intruccion de este comando es la siguiente:

- Cuenta

#####Reportar N
- El comando Reportar N permite generar un documento html el cual se abrira automaticamente en nuestro navegador predeterminado.
En este se mostrara una tabla con la cantidad de registros ingresada como N en el comando.

- La intruccion de este comando es la siguiente:

- Reportar 3
