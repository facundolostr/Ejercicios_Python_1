"""
Escribir un programa que permita resolver el siguiente problema:

Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).

Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.
"""


socio1 = input("Ingrese su nombre: ")
capital1 = float (input ("Ingrese su aporte: "))


socio2 = input("Ingrese su nombre: ")
capital2 = float (input ("Ingrese su aporte: "))


socio3 = input("Ingrese su nombre: ")
capital3 = float (input ("Ingrese su aporte: "))

total_aportado = capital1 + capital2 + capital3

Porcentaje1 = round ((capital1 / total_aportado ) * 100, 2)
Porcentaje2 = round ((capital2 / total_aportado ) * 100, 2)
Porcentaje3 = round ((capital3 / total_aportado ) * 100, 2)

print(f"{socio1} aporto el: {Porcentaje1}% \n {socio2} aporto el: {Porcentaje2}% \n {socio3} aporto el: {Porcentaje3}% \n ")
