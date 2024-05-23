"""
Ejercicio 36

Escribir un programa que permita ingresar dos numeros enteros y la operacion a realizar ('+', '-' . '*', '/'). Debe mostrarse el resultado para la operacion indresada. Considarar que no se puede divir por cero (en ese coso mostrar el texto 'ERROR')

"""


n1 = int(input("Operando 1: "))
n2 = int(input("Operando 2: "))
op = input("Operacion 1: ")
texto = f"{n1} {op} {n2} = "

if op in "+-*/":
    if op == '+':
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    else:
        if n2 == 0: 
            resultado = "ERROR"
        else:
            resultado = n1/n2
    texto += str(resultado)
else:
    texto += "ERROR" 

print (texto)