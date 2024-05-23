"""
Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.

Ejemplo:

4*3 = 4 + 4 + 4 (4 sumado 3 veces).
3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).
"""


n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero que lo multiplique: "))
resultado = 0
explicacion = ''

for num in range(n2):
    resultado += n1 
    explicacion += f"{n1} + "


explicacion = explicacion.rstrip(' + ')
print(f"{n1}*{n2} = {explicacion} = {resultado}" )