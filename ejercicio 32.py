"""
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.

Tiene la siguiente tarifa:

Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

"""

VIAJE_MINIMO = 50
VIAJE_10 = 20
VIAJE_10_MAS = 15

km_recorrido = int(input("Indique la cantidad recorrida: "))
total = 0

if km_recorrido < 10:
    total = VIAJE_MINIMO + (VIAJE_10 * km_recorrido)
else:
    total = VIAJE_MINIMO + (VIAJE_10_MAS * km_recorrido)

print("El total a pagar es: ",total)


