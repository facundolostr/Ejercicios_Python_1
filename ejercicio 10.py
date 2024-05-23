"""
Escribir un programa para resolver el siguiente problema:

Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.

Como pensarlo:
Solicitar al usuario que ingrese las cantidades invertidas por cada persona en tres variables numéricas.
inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))
inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))
inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

Calcular el total de la inversión sumando las cantidades de las tres personas.
total = inversion_persona1 + inversion_persona2 + inversion_persona3

Calcular el porcentaje que representa la inversión de cada persona en relación al total de la inversión.
Dividir la cantidad invertida por cada persona entre el total de la inversión y multiplicar por 100 para obtener el porcentaje. Almacenar el resultado en una variable correspondiente a cada persona. Opcionalmente, se puede redondear el resultado a un número determinado de decimales utilizando la función round().
Ejemplo:

porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2) 
Mostrar por pantalla el porcentaje de inversión de cada persona.

"""
inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))

inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))

inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

total = inversion_persona1 + inversion_persona2 + inversion_persona3

porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)

porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)

porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2) 

print(f"Lo que invirtio la persona 1 fue: {porcentaje_inversion_persona1}% \n Lo que invirtio la persona 2 fue: {porcentaje_inversion_persona2}% \n Lo que invirtio la persona 3 fue: {porcentaje_inversion_persona3}%")