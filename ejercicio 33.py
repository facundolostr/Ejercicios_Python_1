"""
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
"""

DESCUENTO_MENOR = 4.5

DESCUENTO_ENTRE = 8

DESCUENTO_MAYOR= 10.5

importe = float(input("Ingrese el importe de compra: "))
total = 0

if importe < 5500:
    total = importe - (importe*DESCUENTO_MENOR)/100
    print(f"Para el importe de: ${importe}, se aplica un descuento del {DESCUENTO_MENOR} y queda a pagar: ${total}")
elif importe >= 5500 and importe <= 10000:
    total = importe - (importe*DESCUENTO_ENTRE)/100
    print(f"Para el importe de: ${importe}, se aplica un descuento del {DESCUENTO_ENTRE} y queda a pagar: ${total}")
else:
    total = importe - (importe*DESCUENTO_MAYOR)/100
    print(f"Para el importe de: ${importe}, se aplica un descuento del {DESCUENTO_MAYOR} y queda a pagar: ${total}")









