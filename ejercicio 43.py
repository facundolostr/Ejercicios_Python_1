"""
Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.
"""

contador = 0
numeros = 0

while numeros < 100:
    numero_ingresado = int(input("Ingrese un numero que quiera sumar: "))
    numeros += numero_ingresado
    contador += 1
    print(f"la suma es de: {numeros}")

print(f"Numeros ingresados al final: {contador}")


