"""
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.
"""

def es_Igual(n1:int,n2:int)->bool:
    if n1 == n2:
        return True
    else:
        return False



def main():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))

    if es_Igual (n1, n2):
        print("Estos numeros son iguales")
    else:
        print("Son distintos")



main()




