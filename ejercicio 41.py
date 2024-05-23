"""
Ejercicio 41
Escribir un programa que lea numeros enteros hasta que se ingrese un 0,
y muestre el maximo

"""

from random import randint

maximo = -float('inf')
numero = randint(-1000, 1000)
contador = 0
while numero != 0:
    contador += 1
    if numero > maximo:
        maximo = numero
    numero = randint(-1000, 1000)

print (f"Maximo: {maximo} de {contador} numeros generados")

