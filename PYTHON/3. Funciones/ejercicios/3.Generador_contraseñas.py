"""
Ejercicio 03: Generador de contraseñas
Crear un sistema que genere una contraseña aleatoria
Para solucionar este problema se requiere listas, listas mayúsculas, lista de minúsculas, lista de números y lista de símbolos y luego armar una contraseña aleatoria sacando caracteres de estas listas.
"""

import random


def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    simbolos = ['#', '$', '%', '&']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []

    # Generar 15 caracteres aleatorios
    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    # Convertir a una cadena
    password = "".join(password)
    return password


def main():
    password = generar_password()
    print(f'La contraseña generada es: {password}')


if __name__ == '__main__':
    main()
