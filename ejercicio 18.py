"""
Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar.

Pensando los pasos para resolver el problema:

Pedir al usuario que ingrese un número entero.
Almacenar ese número en una variable.
Verificar si el número es par o impar.
Si el número es par, mostrar un mensaje indicando que es par.

Si el número es impar, mostrar un mensaje indicando que es impar.

(Para verificar si un número es par o impar, se puede utilizar el operador módulo (%). Si el resto de la división del número por 2 es 0, entonces el número es par. Si el resto de la división del número por 2 es 1, entonces el número es impar.)

"""



def es_Par (numero):
    if numero%2 == 0:
        return True
    else:
        return False 

def main():
    numero= int(input("Ingrese un numero: "))
    
    if es_Par(numero):
        print("Tu numero es par")
    else:
        print("Tu numero es impar")



main()

