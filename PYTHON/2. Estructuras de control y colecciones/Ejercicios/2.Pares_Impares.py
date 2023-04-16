"""
Crea 2 listas y una tupla que tendrá números de 1 a 9. La primera lista
se llamará pares, y la segunda impar, ambos estarán vacios. Después 
multiplica cada uno de los números de la tupla por un número aleatorio 
entre 1 a 100, si el resultado es par, guarda ese número en la lista de pares,
y si es impar en la lista de impares. Mostrar por consola: 
 - La multiplicación que se produce junto con su resultado con el formato: 2x3=6,
 y la lista de pares e impares
"""

import random

pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for n in numeros:
    numero_random = random.randint(1, 100)
    resultado = n * numero_random

    if resultado % 2 == 0:
        print(f"{n} x {numero_random} = {resultado}")
        pares.append(resultado)
    else:
        print(f"{n} x {numero_random} = {resultado}")
        impares.append(resultado)

print(f"Lista de pares: {pares}")
print(f"Lista de impares: {impares}")
