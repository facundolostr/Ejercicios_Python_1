"""
Ejercicio 40

Escribir un programa que permita ingresar dos numeros a y b. Donde a <= b

El programa debe mostrar:
la suma de los numeros pares de a y b
El producto de los numeros impares entre a y b


"""

a= int (input("Ingrese un valor para a: "))
b= int (input("Ingrese un valor para b: "))

while a > b : #ERROR
    print (f"ERROR: {a} tiene que ser <= {b}")
    b  = int (input("Ingrese un valor para b: "))

suma_pares = 0
producto_impares = 1
for numero in range (a,b+1):
    print (numero, end=',')
    if numero % 2 == 0:
        suma_pares += numero
    else: 
        producto_impares *= numero
print()
print(f"Suma de pares: {suma_pares}")
print(f"Producto de impares: {producto_impares}")


