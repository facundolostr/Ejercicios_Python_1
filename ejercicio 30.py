"""
Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)



"""




def main():

    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese un numero: "))

    mayor = -float('inf')
    menor = float ('inf')

    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

    resto = mayor%menor

    print(f"Mayor: {mayor} y Menor: {menor}")

    if resto == 0:
        print(f"{mayor} es divisible por {menor}")
    else:
        print(f"{mayor} no es divisible por {menor}")





main()



