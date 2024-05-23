"""Ejercicio 35

Existen dos reglas que identifican dos conjuntos de valores_
a) El numero es de un solo digito.
b) El numero es impar

A partir de estas reglas, escribir un programa que permita inresar un numero entero.
Debe adignar el valor que corresponda a las vareable booleanas: 
EsDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno

El valor Verdadero o falso, segun corresponda, para indicar si el valor numero ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios numeros y probar el algoritmo, escribiendo los resultados.
"""
numero = int(input("Numero: "))


#a) El numero es de un solo digito.
EsDeUnSoloDigito = numero >= -9 and numero <= 9

#b) El numero es impar
esImpar = (numero%2) != 0
5
#a) y b)
estaEnAmbos= EsDeUnSoloDigito and esImpar


noEstaEnNinguno = not EsDeUnSoloDigito and not esImpar

cartel = f"""
numero {numero}
EsDeUnSoloDigito {EsDeUnSoloDigito}
esImpar {esImpar}
estaEnAmbos {estaEnAmbos}
noEstaEnNinguno {noEstaEnNinguno}
"""

print (cartel)