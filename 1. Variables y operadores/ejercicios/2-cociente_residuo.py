"""
Calcular el cociente y residuo.
Enunciado: Hallar el cociente y residuo de dos números enteros.
Para ello, se requiere que el usuario ingrese 2 números enteros
y el sistema realice el calculo respectivo para hallar el cociente
y el residuo
"""

print("Calcular el cociente y residuo de dos números")
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

cociente = a//b
residuo = a % b
print(f"El Cociente es: {cociente} y el Residuo es: {residuo}")
