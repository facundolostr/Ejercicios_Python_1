"""
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""


def validacion_edad(edad):
    if edad < 1 or edad > 120:
        return print("edad invalida"), exit()
    else:
        return True

def validacion_genero (genero):
    if genero != "m"  and genero != "f":
        return print ("Genero invalido"), exit()
    else:
        return True



def main():
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    genero = str(input("Ingrese su genero: "))
    jubilacion = False




    if edad >= 60 and genero == "f":
        jubilacion = True
    elif edad >= 65 and genero == "m":
        jubilacion = True


    if validacion_edad(edad) and (validacion_genero(genero)) and jubilacion:
        print (f"{nombre} se puede jubilar")
    else:
        print (f"{nombre} todavia no se puede jubilar")


main()