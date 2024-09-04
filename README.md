# Federico Suarez Moreno, Cohort 13

# Urban Grocers API Testing Project

## Descripción

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, específicamente para la funcionalidad de creación de kits de usuario,
incluyendo la validación de nombres de kit y registro de usuario.

## Entorno

1. Pycharm
2. Pytest
3. Libreria requests

# Instrucciones

1. Instalar la libreria request a traves la consola con el siguiente comando :pip install requests
2. Instalar pytest a traves de la consola con el siguente comando : pip install pytest
3. Actualizar la url del servidor y verificar que los endpoints sean correctos
4. Realizar los test con la herramienta pytest 

# Pruebas

1. 	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
2.	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
3.	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
4.	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
5.	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
6.	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
7.	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
8.	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
9.	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400
