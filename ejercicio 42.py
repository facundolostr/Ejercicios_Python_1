"""
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

"""


suma = 0
contador = 0


while True:
    numero = int(input("Ingrese un número entero (o 0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1


if contador > 0:
    promedio = suma / contador
    print(f"El promedio de los números ingresados es: {promedio}")
else:
    print("No se ingresaron números para calcular el promedio.")
