"""Ejercicio 026

Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon.
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse."""


cant_invitados = int (input("Cantidad de invitados: "))
cant_asientos = int (input ("cantidad de asientos: "))

asientos_totales = cant_invitados - cant_asientos

if cant_invitados <= cant_asientos:
    print("Hay asientos suficientes")
elif cant_invitados > cant_asientos:
    print("faltan ", asientos_totales , "asientos")



