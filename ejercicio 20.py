"""
Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.
"""


def str_Iguales(cadena1, cadena2):
    if cadena1 == cadena2:
        return True
    else:
        return False






def main():
    cadena1 = str(input("Escribe una cadena de caracteres"))
    cadena2 = str(input("Escribe otra cadena de caracteres"))

    if str_Iguales(cadena1, cadena2):
        print("Son iguales")
    else:
        print("Son distintos")



main()

