"""Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.

Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

¿Sobran datos? ¿Qué datos sobran?"""

nombre = input("Ingrese el nombre del vendedor: ")
salario_base = float(input("Ingrese el salario base del empleado: "))
valor_ventas = float (input ("ingrese la cantidad de ventas que realizo: "))

porcentaje_ventas = (valor_ventas * 5) / 100
salario_final = salario_base + porcentaje_ventas

print(f"El empleado {nombre} le corresponde {salario_final} de sueldo este mes")



