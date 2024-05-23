"""
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

"""


def main():

    mes = int(input("Ingrese el numero de un mes: "))

    if mes == 1:
        print ("enero")
    elif mes == 2:
        print ("febrero")
    elif mes == 3:
        print ("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print ("Mayo")
    elif mes == 6:
        print("Junio")
    elif mes == 7:
        print ("Julio")
    elif mes == 8:
        print ("Agosto")
    elif mes == 9:
        print ("Septiembre")
    elif mes == 10:
        print ("Ocubre")
    elif mes == 11:
        print ("Noviembre")
    elif mes == 12:
        print ("Diciembre")
    else:
        print("Ingrese un mes valido")







main()