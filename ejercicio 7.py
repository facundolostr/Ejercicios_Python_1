"""
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:

a. Multiplicado por 10. (utilizar el operador *) a. Dividido por 10. (utilizar el operador /) a. Elevado al cuadrado. (utilizar el operador **)

Cada resultado debe mostrarse en una línea distinta.

Ejemplo de ejecución:

Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""

num = int(input("Ingrese un numero: "))
mul = (num * 10)
div = float(num / 10)
Elev = (num ** 2)

print (f" {num} * 10 = {mul} \n {num} / 10 = {div} \n {num} ** 2 = {Elev}")