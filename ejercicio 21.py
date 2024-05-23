"""
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.
"""

def es_Mayor(n1,n2):
    if n1 > n2:
        return True
    else:
        return False

def es_Menor(n1,n2):
    if n1 < n2:
        return True
    else:
        return False



def main():
    n1 = int(input("Escribe un numero: "))
    n2 = int(input("Esbribe otro numero: "))

    if es_Mayor(n1,n2):
        print(f"{n1} es mayor que {n2}")
    elif es_Menor(n1,n2):
        print(f"{n1} es menor que {n2}")
    else:
        print(f"{n1} es igual que {n2}")
        





main()

