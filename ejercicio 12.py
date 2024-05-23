"""
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.

Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."

Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?
¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""

angulo1 = int(input("Ingrese el primer angulo: "))
angulo2 = int(input("Ingrese el segundo angulo: "))
angulo_restante = 180 - (angulo1 + angulo2)

if (angulo1 or angulo2) < 0:
    print ("ERROR, ingrese un numero mayor a 0")
elif angulo_restante >= 180 or angulo_restante <= 0:
    print ("ERROR, la suma de los 2 angulos ingresados deben ser menores a 180 grados ") 
else:
    print (f"El tercer angulo es: {angulo_restante}")
