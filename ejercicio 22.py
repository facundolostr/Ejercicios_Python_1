"""
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""

def es_Mayor (n1,n2,n3):

    mayor = -float('inf')

    if n1 >= n2 and n1 >= n3:
        mayor = n1
    elif n2 >= n1 and n2 >= n3:
        mayor = n2
    else: 
        mayor = n3


    return mayor


def main():

    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese un numero: "))
    n3 = int(input("Ingrese un numero: "))


    print(f"{es_Mayor(n1,n2,n3)} es el mayor")
    


main()