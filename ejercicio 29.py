""" Ejercicio 29

Escribir un programa que permita ingresa las notas de los dis parciales de un alumno e indicar si promociono, aprobo o de recuperar.

Si el valor de la nota no esta entre 0 y 10, debe informar un error

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

nota1 = float(input ("Nota1: "))
nota2 = float(input ("Nota2: "))
cartel = "No aprobado"
error_datos = nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10

if not error_datos:
    aprueba = nota1 >= 4 and nota2 >= 4
    recupera = not aprueba
    promociona = nota1 >= 7 and nota2 >= 7

    if aprueba:
        cartel = "Aprueba"
    if promociona:
        cartel += " con promociono"
else:
    print ("Error de datos")
    exit()


print({cartel})