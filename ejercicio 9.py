"""
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.

Como pensarlo:

Pedir al usuario que ingrese un valor para la variable num1.

Pedir al usuario que ingrese un valor para la variable num2.

Mostrar por pantalla el valor de las variables num1 y num2.

Intercambiar los valores de las variables num1 y num2.

Mostrar por pantalla el valor de las variables num1 y num2.


"""

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

print (f"numero 1: {n1}, numero 2: {n2}")

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print (f"numero 1: {n1}, numero 2: {n2}")




