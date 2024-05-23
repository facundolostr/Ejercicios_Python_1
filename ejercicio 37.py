"""
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.

"""



def main ():

    i = 1

    while i <= 5:
        print(i)
        i += 1

    print("\n")

    for i in range(5, 0 , -1):
        print (i)

main()